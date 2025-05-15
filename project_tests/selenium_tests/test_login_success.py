import unittest
import multiprocessing
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from app import create_app, db
from models import UserModel
from config import TestConfig
from assertpy import assert_that


localHost = 'http://127.0.0.1:5000/'

class SeleniumLoginTest(unittest.TestCase):
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

    def test_login_success(self):
        self.driver.get(localHost+"auth/login")
        time.sleep(5)

        #Fill in login form -- email, password, login-btn
        self.driver.find_element(By.ID, 'uwa_email').send_keys('selenium@student.uwa.edu.au')
        self.driver.find_element(By.ID, 'password').send_keys('testpassword123')
        self.driver.find_element(By.ID, 'login-btn').click()
        time.sleep(5)

        assert_that(self.driver.current_url).is_equal_to(localHost)
        assert_that(self.driver.page_source).does_not_contain('window.loginError = Invalid email or password";')


    def tearDown(self):
        self.server_thread.terminate()
        self.driver.close()
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

        