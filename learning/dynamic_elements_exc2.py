from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
   driver.get("https://the-internet.herokuapp.com/dynamic_controls")
   wait = WebDriverWait(driver,10)

   remove_btn = driver.find_element(By.XPATH, "//button[text()='Remove']")
   remove_btn.click()

   wait.until(
       EC.invisibility_of_element_located((By.ID, "checkbox"))
   )
   print("Checkbox Dissapeared")

   input_box = driver.find_element(By.CSS_SELECTOR, "input[type='text']")

   print("The input box is",input_box.is_enabled())

   enable_btn = driver.find_element(By.XPATH,"//button[text()='Enable']")
   enable_btn.click()

   wait.until(
       EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']"))
   )
   input_box.send_keys("I'm In")
   
   print("the input box is",input_box.is_enabled())

   add_btn = driver.find_element(By.XPATH, "//button[text()='Add']")

   add_btn.click()

   checkbox1 = wait.until(
       EC.element_to_be_clickable((By.ID,"checkbox"))

   )
   print("Checkbox is displayed:",checkbox1.is_displayed())

   checkbox1 = driver.find_element(By.ID, "checkbox")
   checkbox1.click()
   time.sleep(5)


finally:
    driver.quit()
