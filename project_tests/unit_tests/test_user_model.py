import unittest
from app import create_app
from exts import db
from config import TestConfig
from models import UserModel
from assertpy import assert_that

class TestUserModel(unittest.TestCase):
    def setUp(self):
        """Set up the test client and database."""
        testApp = create_app(TestConfig)
        self.app_context = testApp.app_context()
        self.app_context.push()
        db.create_all()

        # Create a test user
        self.test_user = UserModel(
            username='testuser',
            uwa_email = 'test@uwa.edu.au',
            age=20,
            gender='Male'
        )
        self.test_user.password = 'testpassword123'  # Set the password using the setter

        db.session.add(self.test_user)
        db.session.commit()

        self.client = testApp.test_client()

    def tearDown(self):
        """Clean up after each test."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        assert_that(self.test_user.password_hash).is_not_equal_to('testpassword123')
        assert_that(self.test_user.verify_password('testpassword123')).is_true()
        assert_that(self.test_user.verify_password('wrongpassword')).is_false()