from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/login")

# Input username
username = driver.find_element(By.NAME, "username")
username.send_keys("tomsmith")

# Input password
password = driver.find_element(By.CSS_SELECTOR, "input#password")
password.send_keys("SuperSecretPassword!")

# Click login button
login_button = driver.find_element(By.XPATH, "//*[@id='login']/button")
login_button.click()
time.sleep(5)

driver.quit()