import unittest
from assertpy import assert_that
from datetime import date
from app import create_app
from config import TestConfig
from exts import db
from models import UserModel, SpotModel, CategoryModel, collectionModel, TendencyModel

class LikeRouteTests(unittest.TestCase):
    def setUp(self):
        """Set up the test client and database."""
        testApp = create_app(TestConfig)
        self.app_context = testApp.app_context()
        self.app_context.push()
        db.create_all()

        self.client = testApp.test_client()

        # Create test user
        self.test_user = UserModel(
            username='testuser',
            uwa_email='blank@uwa.edu.au',
            age=20,
            gender='Male',
        )
        self.test_user.password = 'testpassword123'
        db.session.add(self.test_user)

        # Create and commit the category first to get its ID
        self.test_category = CategoryModel(name='Test_Category')
        db.session.add(self.test_category)
        db.session.commit()  

        # Create and commit the spot using real category_ID
        self.test_spot = SpotModel(
            spot_name='Test_Spot',
            category_ID=self.test_category.category_ID 
        )
        db.session.add(self.test_spot)
        db.session.commit()  

        # Simulate logged-in user
        with self.client.session_transaction() as sess:
            sess['_user_id'] = str(self.test_user.id)

    def tearDown(self):
        """Clean up after each test."""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_like_spot(self):
        response = self.client.get(f'/index/like/{self.test_spot.spot_ID}') 
        assert_that(response.status_code).is_equal_to(200)

        data = response.get_json()
        assert_that(data).is_length(1)

        liked = data[0]
        assert_that(liked['name']).is_equal_to('Test_Spot')
        assert_that(liked['likes']).is_equal_to(1)
        assert_that(liked['spotid']).is_equal_to(self.test_spot.spot_ID)

        #Database check
        liked_spot = collectionModel.query.filter_by(user_id=self.test_user.id, item_ID=self.test_spot.spot_ID).first()
        assert_that(liked_spot).is_not_none()

        updated_spot = SpotModel.query.filter_by(spot_ID=self.test_spot.spot_ID).first()
        assert_that(updated_spot.num_likes).is_equal_to(1)

        updated_category = CategoryModel.query.filter_by(category_ID=self.test_category.category_ID).first()
        assert_that(updated_category.total_likes).is_equal_to(1)

        tendency = TendencyModel.query.filter_by(category_ID=self.test_category.category_ID, snapshot_date=date.today()).first()
        assert_that(tendency).is_not_none()
        assert_that(tendency.like_count).is_equal_to(1)