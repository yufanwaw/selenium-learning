from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/checkboxes")

# Wait until checkboxes are present
box1 = driver.find_element(By.CSS_SELECTOR, "#checkboxes input:nth-of-type(1)")
box2 = driver.find_element(By.CSS_SELECTOR, "#checkboxes input:nth-of-type(2)")

if  not box1.is_selected():
    box1.click()

# Ensure second checkbox is unchecked
if  box2.is_selected():
    box2.click()

time.sleep(5)
driver.quit()