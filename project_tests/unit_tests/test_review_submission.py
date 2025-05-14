import unittest
from assertpy import assert_that
from app import create_app
from config import TestConfig
from exts import db
from models import UserModel, SpotModel, reviewstModel, CategoryModel

class InsertReviewTestCase(unittest.TestCase):
    def setUp(self):
        testApp = create_app(TestConfig)
        self.app_context = testApp.app_context()
        self.app_context.push()

        db.create_all()

        # Create dummy user and spot
        self.user = UserModel(
            username="testuser",
            uwa_email="test@uwa.edu.au",
            age=20,
            gender="male",
        )
        self.user.password = "testpass"
        db.session.add(self.user)
        db.session.commit()

        self.category = CategoryModel(name="Test Category")
        db.session.add(self.category)
        db.session.commit()

        self.spot = SpotModel(
            spot_name="Test Spot",
            category_ID=self.category.category_ID,
            locationx=0.0,
            locationy=0.0,
            description="A test spot",
            num_likes=0
        )
        db.session.add(self.spot)
        db.session.commit()

        self.client = testApp.test_client()

        # Simulate login by injecting user_id into session
        with self.client.session_transaction() as sess:
            sess['_user_id'] = str(self.user.id)

    def test_insert_review_success(self):
        form_data = {
            "cleanliness": "5",
            "atmosphere": "4",
            "comfort": "3",
            "accessibility": "4",
            "value": "3",
            "service_quality": "4",
            "noise_level": "2",
            "crowdedness": "2",
            "visit_frequency": "5",
            "comment": "Nice spot"
        }

        response = self.client.post(
            f"/index/insert_review/{self.spot.spot_ID}",
            data=form_data
        )

        assert_that(response.status_code).is_equal_to(204)

        # Check that review was saved in DB
        review = reviewstModel.query.filter_by(user_id=self.user.id, spot_ID=self.spot.spot_ID).first()

        assert_that(review).is_not_none()
        assert_that(review.text).is_equal_to("Nice spot")
        assert_that(review.rank_cleanliness).is_equal_to(5)
        assert_that(review.rank_atmosphere).is_equal_to(4)

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()