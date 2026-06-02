from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    wait = WebDriverWait(driver, 10)

    # Click Remove button
    remove_btn = driver.find_element(By.XPATH, "//button[text()='Remove']")
    remove_btn.click()

    # Wait until checkbox disappears
    wait.until(
        EC.invisibility_of_element_located((By.ID, "checkbox"))
    )

    print("Checkbox disappeared")

    

    # Check the text field before clicking Enable.
    input_box = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    print("Input enabled before clicking Enable:", input_box.is_enabled())

    # Click Enable and wait until the text field becomes clickable.
    enable_btn = driver.find_element(By.XPATH, "//button[text()='Enable']")
    enable_btn.click()

    input_box = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='text']"))
    )

    print("Input enabled after clicking Enable:", input_box.is_enabled())
    input_box.send_keys("Hello QA")

    # Click Disable and wait until the text field becomes disabled again.
    disable_btn = driver.find_element(By.XPATH, "//button[text()='Disable']")
    disable_btn.click()

    wait.until(
        lambda browser: not browser.find_element(
            By.CSS_SELECTOR, "input[type='text']"
        ).is_enabled()
    )

    input_box = driver.find_element(By.CSS_SELECTOR, "input[type='text']")
    print("Input enabled after clicking Disable:", input_box.is_enabled())

finally:
    driver.quit()
