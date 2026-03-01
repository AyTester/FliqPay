# from selenium import webdriver 
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
import time
# import configparser
# from selenium.common.exceptions import TimeoutException 

# class Base:
#     def __init__(self, email, password):
#         self.driver = webdriver.Chrome(ChromeDriverManager().install())
#         time.sleep(2)
#         self.driver.maximize_window()
#         self.email = email
#         self.password = password


#     def wait_for_element(self, by, value, timeout=10):
#         return WebDriverWait(self.driver, timeout).until(
#             EC.element_to_be_clickable((by, value))
#         )

#     def user_login(self, url, email, password):
#         self.driver.get(url)
#         email_field = self.wait_for_element(By.NAME, "email")
        
#         password_field = self.wait_for_element(By.ID, "password")
        
        
#         keep_me_signed_in_checkbox = self.wait_for_element(By.XPATH, "//*[@id='__nextb']/div/div/div/[2]/div/div/div[2]/form/div[4]")
#         keep_me_signed_in_checkbox.click()
#         time.sleep(2)

#         login_button = self.wait_for_element(By.XPATH, "//html/body/div/[1]/div/div/div[3]/div/div/div[2]/form/button")
#         login_button.click()

        


# def main():
#     config = configparser.ConfigParser()
#     config.read("config.ini")
#     email = config.get("Credentials", "email")
#     password = config.get("Credentials", "password")

#     base = Base(email, password)
#     base.user_login("https://sandbox.fincra.com/")

# # if __name__ == "__main__":
# #     main()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class Base:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def wait_for_element(self, by, value, timeout=20):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def user_login(self, url, email, password):
        self.driver.get(url)
        email_field = self.wait_for_element(By.NAME, "email")
        email_field.send_keys(email)

        password_field = self.wait_for_element(By.ID, "password")
        password_field.send_keys(password)

        login_button = self.wait_for_element(By.XPATH, "//button[contains(text(),'Log In')]")
        login_button.click()

