from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class Dashboard:
    def __init__(self, driver):
        self.driver = driver

    

    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        # Add all actions you want to perform on the dashboard here

    def user_dashboard(self):
        self.driver.refresh()
        print('I have refreshed the page')

        startonboarding_button = self.wait_for_element(By.XPATH, "//button[contains(@class,'lg:mx-0 mx-3 md:w-1/3 md:py-5 flex items-center bg-violet-600 px-5 py-4 text-white no-underline rounded-lg font-medium shadow-md justify-center')]")
        startonboarding_button.click()                            
        time.sleep(5)

        # self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(2)  
        # self.driver.execute_script("window.scrollTo(0, 0);")

        back_button = self.wait_for_element(By.XPATH, "//a[contains(@class,'flex justify-center w-32 px-3 py-2 transition ease-in-out bg-white border rounded-md gap-x-3 border-gray-2 hover:bg-primary-dark hover:text-white duration-400')]")
        back_button.click()  
        time.sleep(5)

        overview_button = self.wait_for_element(By.XPATH, "/html/body/div[1]/div/div/nav/div/ul[2]/li[1]/a")
        overview_button.click()
        time.sleep(5)

        balances_button = self.wait_for_element(By.XPATH, "//span[contains(text(),'balances')]")
        balances_button.click()
        time.sleep(5)


        payIns_dropdown = self.wait_for_element(By.XPATH, "//button[contains(@class,'border-transparent hover:bg-gray-200 cursor-pointer capitalize px-4')]//div[contains(@class,'ml-auto')]//*[name()='svg']//*[name()='path' and contains(@fill,'currentCol')]")
        payIns_dropdown.click()
        time.sleep(2)

        history_button = self.wait_for_element(By.XPATH, "//span[contains(text(),'history')]")
        history_button.click()
        time.sleep(5)

        payIns_dropdown = self.wait_for_element(By.XPATH, "//button[contains(@class,'bg-purple-200 text-purple-700 border-purple-700 cursor-pointer capitalize px-4')]")
        payIns_dropdown.click()
        time.sleep(2)


        payOuts_dropdown = self.wait_for_element(By.XPATH, "//li[@class='tour-step-3']//button[1]")
        payOuts_dropdown.click()
        time.sleep(5)

        makePayout_button = self.wait_for_element(By.XPATH, "//span[contains(text(),'make payout')]")
        makePayout_button.click()
        time.sleep(5)

        payOuts_dropdown = self.wait_for_element(By.XPATH, "//li[@class='tour-step-3']//button[1]")
        payOuts_dropdown.click()
        time.sleep(5)

        conversions_button = self.wait_for_element(By.XPATH, "//span[contains(text(),'conversions')]")
        conversions_button.click()
        time.sleep(5)

        cancel_button = self.wait_for_element(By.XPATH, "//button[contains(@class,'font-medium text-secondary')]")
        cancel_button.click()
        time.sleep(5)
        

        settlements_button = self.wait_for_element(By.XPATH, "//span[contains(text(),'settlements')]")
        settlements_button.click()
        time.sleep(5)

        usersAndRoles_button = self.wait_for_element(By.XPATH, "//a[contains(@href,'/user-management')]")
        usersAndRoles_button.click()
        time.sleep(5)

        
        
        

    
    
