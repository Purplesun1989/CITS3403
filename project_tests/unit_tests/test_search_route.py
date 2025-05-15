import unittest
from assertpy import assert_that
from app import create_app
from config import TestConfig
from exts import db
from models import SpotModel

class SearchRouteTests(unittest.TestCase):
    def setUp(self):
        """Set up the test client and database."""
        testApp = create_app(TestConfig)
        self.app_context = testApp.app_context()
        self.app_context.push()
        db.create_all()
        self.client = testApp.test_client()

        # Create a test spot
        self.test_spot = SpotModel(
            spot_name='Test_Spot',
            category_ID=1,
        )
        db.session.add(self.test_spot)
        db.session.commit()

    def tearDown(self):
        """Clean up after each test."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_search_route(self):
        payload = {'inputValue': 'Test_Spot'}
        response = self.client.post('/index/search', json=payload)

        assert_that(response.status_code).is_equal_to(200)
        result = response.get_json()

        assert_that(result).is_not_empty()
        assert_that(result['spot_id']).is_equal_to(self.test_spot.spot_ID)


    def test_search_route_no_results(self):
        payload = {'inputValue': 'Non_Existent_Spot'}
        response = self.client.post('/index/search', json=payload)

        assert_that(response.status_code).is_equal_to(200)
        result = response.get_json()

        assert_that(result['spot_id']).is_none()