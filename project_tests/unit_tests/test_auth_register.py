import unittest
from assertpy import assert_that
from app import create_app
from exts import db
from config import TestConfig
from models import UserModel

class AuthRegisterTests(unittest.TestCase):
    def setUp(self):
        """Set up the test client and database."""
        testApp = create_app(TestConfig)
        self.app_context = testApp.app_context()
        self.app_context.push()
        db.create_all()
        self.client = testApp.test_client()

    def tearDown(self):
        """Clean up after each test."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register_success(self):
        response = self.client.post('/auth/register', data={
            'register_username': 'newuser',
            'register_email': 'new@student.uwa.edu.au',
            'register_password': 'strongpass123',
            'register_birthday': '2000-01-01',
            'gender': 'male'
        }, follow_redirects=True)

        assert_that(response.status_code).is_equal_to(200)

        user = UserModel.query.filter_by(uwa_email="new@student.uwa.edu.au").first()
        assert_that(user).is_not_none()
        assert_that(user.username).is_equal_to("newuser")