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

    wait = WebDriverWait(driver, 10)
    remove_btn = driver.find_element(By.XPATH, "//button[text()='Remove']")
    remove_btn.click()
    
    wait.until(
        EC.invisibility_of_element_located((By.ID, "checkbox"))
    )
   
    print("Checkbox disappeared")

    input_box = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
   
    print("Input enabled before clicking Enable:", input_box.is_enabled())

    enable_btn = driver.find_element(By.XPATH, "//button[text()='Enable']")
    enable_btn.click()

    input_box = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']"))
    )

    print("Input enabled before clicking Enable:", input_box.is_enabled())

    input_box.send_keys("Testing")

    disable_btn = driver.find_element(By.XPATH, "//button[text()='Disable']")
    
    disable_btn.click()

    wait.until(
        lambda browser: not browser.find_element(
            By.CSS_SELECTOR,"input[type='text']"
        ).is_enabled()
    )
    
    input_box = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    print("Input enabled before clicking Enable:", input_box.is_enabled())


    #Click Add button to show the checkbox
    add_btn = driver.find_element(By.XPATH, "//button[text()='Add']")
    add_btn.click()

    checkbox = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#checkbox")
        )
    )
    checkbox.click()
    wait.until(
        lambda browser: checkbox.is_selected()
    )
    print("Checkbox is selected:", checkbox.is_selected())

    time.sleep(5)

finally:
    driver.quit()
