from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SecurePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    logout_button = (By.CSS_SELECTOR, "a.button.secondary.radius")
    flash_message = (By.ID, "flash")

    # Actions
    def click_logout(self):
        self.wait.until(EC.element_to_be_clickable(self.logout_button)).click()

    def get_flash_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.flash_message)).text
    

