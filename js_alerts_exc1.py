from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

wait = WebDriverWait(driver, 10)


driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()

alert = wait.until(EC.alert_is_present())

time.sleep(2)

print("Alert Text:",alert.text)

alert.accept()

print("test",driver.find_element(By.ID, "result").text)


driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()

alert = wait.until(EC.alert_is_present())

alert.send_keys("Test ajah")
time.sleep(3)

alert.accept()

print("test",driver.find_element(By.ID, "result").text)





