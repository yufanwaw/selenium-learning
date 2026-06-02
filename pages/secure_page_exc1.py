from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SecurePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    #locators
    logout_btn = (By.CSS_SELECTOR,"a.button.secondary.radius")
    flash_msg = (By.ID,"flash")

    #actions
    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.logout_btn)).click()

    def get_flash_msg(self):
        return self.wait.until(EC.visibility_of_element_located(self.flash_msg)).text
    
        
