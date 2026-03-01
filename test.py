# import unittest
# from HtmlTestRunner import HTMLTestRunner
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from login_page import Base
# from dashboard_page import Dashboard
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException   
# import time
# import configparser


# class TestSuite(unittest.TestCase):
    
#     @classmethod
#     def setUpClass(cls):
#         config = configparser.ConfigParser()
#         config.read("config.ini")
#         email = config.get("Credentials", "email")
#         password = config.get("Credentials", "password")
        
        
#         cls.base = Base(email, password)
#         cls.dashboard = Dashboard(cls.base.driver)

        

#     def test_user_login(self):
#         self.base.user_login("https://sandbox.fincra.com/", "email", "password")
    
#         # # Wait until the URL changes to the expected URL
#         # expected_url = "https://app.fincra.com/onboarding"
#         # try:
#         #     WebDriverWait(self.base.driver, 20).until(
#         #         EC.url_to_be(expected_url)
#         #     )
#         # except TimeoutException:
#         #     self.fail("The URL did not change to the expected URL within the given time.")
        
#         # # Assert that the current URL is the expected URL
#         # current_url = self.base.driver.current_url
#         # self.assertEqual(current_url, expected_url, 
#         #                  f"URL assertion failed: Expected URL '{expected_url}' but got '{current_url}'")

#     def test_user_dashboard(self):
#         print("Starting test_user_dashboard...")
#         self.dashboard.user_dashboard()
        

#     # def test_user_dashboard(self):
#     #     result = self.dashboard.test_user_dashboard()



# @classmethod
# def tearDownClass(cls):
#     time.sleep(2)
#     cls.base.driver.quit()

# if __name__ == "__main__":
#     unittest.main(testRunner=HTMLTestRunner(
#         output="./report", report_name="FliqPay_Test", report_title="Fliq_Pay_Test"
#         ))




import unittest
from HtmlTestRunner import HTMLTestRunner
from login_page import Base
from dashboard_page import Dashboard
import configparser
import time


class TestSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Load credentials from config.ini
        config = configparser.ConfigParser()
        config.read("config.ini")
        email = config.get("Credentials", "email")
        password = config.get("Credentials", "password")
        
        # Initialize the Base class for login
        cls.base = Base(email, password)
        # Initialize the Dashboard class for dashboard interactions
        cls.dashboard = Dashboard(cls.base.driver)

    def test_user_login(self):
        """Test user login functionality."""
        self.base.user_login("https://sandbox.fincra.com/", self.base.email, self.base.password)
        self.assertIn(
            "dashboard",
            self.base.driver.current_url,
            "Login failed: Dashboard not reached after login."
        )

    def test_user_dashboard(self):
        """Test user dashboard functionality."""
        print("Starting dashboard test...")
        self.dashboard.user_dashboard()

    @classmethod
    def tearDownClass(cls):
        """Close the browser after all tests."""
        time.sleep(2)
        cls.base.driver.quit()


if __name__ == "__main__":
    unittest.main(
        testRunner=HTMLTestRunner(
            output="./report",
            report_name="FliqPay_Test_Report",
            report_title="FliqPay Test Execution Report"
        )
    )
