import unittest
from assertpy import assert_that
from app import create_app
from config import TestConfig
from exts import db
from models import UserModel

class AuthLoginTests(unittest.TestCase):
    def setUp(self):
        """Set up the test client and database."""
        testApp = create_app(TestConfig)
        self.app_context = testApp.app_context()
        self.app_context.push()
        db.create_all()
        self.client = testApp.test_client()

        # Create a test user
        self.test_user = UserModel(
            username='testuser',
            uwa_email='test@uwa.edu.au',
            age=20,
            gender='Male'
        )
        self.test_user.password = 'testpassword123'
        db.session.add(self.test_user)
        db.session.commit()

    def test_login_success(self):
        response = self.client.post('/auth/login', data={
            'uwa_email': 'test@uwa.edu.au',
            'password': 'testpassword123'
        }, follow_redirects=True)

        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.data).does_not_contain(b'window.loginError = "Invalid email or password";')

    def test_login_failure(self):
        """Test login fails with incorrect credentials and error message is injected in JS."""
        response = self.client.post(
            '/auth/login',
            data={
                'uwa_email': 'fake@uwa.edu.au', 
                'password': 'wrongpass'
            },
            follow_redirects=True
        )

        # Check that we stayed on the login page
        assert_that(response.status_code).is_equal_to(200)

        # Relaxed check: confirm JavaScript error injection is present
        assert_that(response.data).contains(b'window.loginError')
        assert_that(response.data).contains(b'Invalid email or password')

    def test_login_missing_fields(self):
        """Test login fails with missing fields (empty email/password)."""
        response = self.client.post(
            '/auth/login',
            data={
                'uwa_email': '',
                'password': ''
            },
            follow_redirects=True
        )

        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.data).contains(b'id="uwa_email"')  # confirm page reloaded

    def test_login_nonexistent_user(self):
        response = self.client.post("/auth/login", data={
            "uwa_email": "test436@uwa.edu.au",
            "password": "any"
        }, follow_redirects=True)

        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.data).contains(b'window.loginError = "Invalid email or password";')

    def tearDown(self):
        """Clean up after each test."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
