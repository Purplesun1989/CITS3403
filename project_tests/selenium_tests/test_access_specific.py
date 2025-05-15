import unittest
import multiprocessing
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

from app import create_app, db
from models import UserModel, SpotModel
from config import TestConfig
from assertpy import assert_that


localHost = 'http://127.0.0.1:5000/'

class LikedSpotsTest(unittest.TestCase):
    def setUp(self):
            testApp = create_app(TestConfig)
            self.app_context = testApp.app_context()
            self.app_context.push()
            db.drop_all()
            db.create_all()

            # Create a test user
            self.test_user = self.addUser(
                username='testuser',
                uwa_email='selenium@student.uwa.edu.au',
                age=22,
                gender='Male',
                password='testpassword123'
            )

            self.test_spot = self.addSpot(
                spot_ID=35,
                spot_name="UWA Library",
                category_ID=6,
                locationx=0.0,
                locationy=0.0,
                description="Silent study area",
                num_likes=0
            )

            multiprocessing.set_start_method("fork")
            self.server_thread = multiprocessing.Process(target=testApp.run)
            self.server_thread.start()
            time.sleep(2)

            options = webdriver.ChromeOptions()
            options.add_argument('--headless=new')
            self.driver = webdriver.Chrome(options=options)

    def addUser(self, username, uwa_email, age, gender, password):
        user = UserModel(
            username=username,
            uwa_email=uwa_email,
            age=age,
            gender=gender
        )
        user.password = password 
        db.session.add(user)
        db.session.commit()
        return user
    
    def addSpot(self, spot_ID, spot_name, category_ID, locationx, locationy, description, num_likes):
        spot = SpotModel(
            spot_ID=spot_ID,
            spot_name=spot_name,
            category_ID=category_ID,
            locationx=locationx,
            locationy=locationy,
            description=description,
            num_likes=num_likes
        )
        db.session.add(spot)
        db.session.commit()
        return spot

    def test_liked_spot_clickable(self):

        self.driver.get(localHost+"auth/login")
        time.sleep(5)

        #Fill in login form -- email, password, login-btn
        self.driver.find_element(By.ID, 'uwa_email').send_keys('selenium@student.uwa.edu.au')
        self.driver.find_element(By.ID, 'password').send_keys('testpassword123')
        self.driver.find_element(By.ID, 'login-btn').click()
        time.sleep(5)

        # Wait for the page to load and liked-box content to appear
        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.CLASS_NAME, "liked-box-content"))
        )

        # Wait for at least one liked spot to be present
        liked_items = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_all_elements_located((By.CLASS_NAME, "liked-box-items"))
        )

        # Click on the first liked spot
        liked_items[0].click()
        time.sleep(5)

        # Check if the URL matches the expected pattern
        assert_that(self.driver.current_url).matches(r"http://127\.0\.0\.1:5000/index/\d+")


    def tearDown(self):
        self.server_thread.terminate()
        self.driver.close()
        db.session.remove()
        db.drop_all()
        self.app_context.pop()