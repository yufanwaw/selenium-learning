from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

wait = WebDriverWait(driver, 10)

# Click "Click for JS Alert"
#driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()

# Wait for alert
#alert = wait.until(EC.alert_is_present())

#print("Alert text:", alert.text)

# Accept alert
#alert.accept()

# Dismiss alert
#alert.dismiss()

# Click "Click for Prompt Alert"
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()

# Wait for alert
alert = wait.until(EC.alert_is_present())

alert.send_keys("Hello QA")
alert.accept()

inputted = driver.find_element(By.ID,"result").text
print("Alert text:", inputted)


driver.quit()