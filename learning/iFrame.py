from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Selenium 4 can manage ChromeDriver automatically.
driver = webdriver.Chrome()

try:
    driver.get("https://the-internet.herokuapp.com/iframe")

    wait = WebDriverWait(driver, 10)

    # Switch to iframe
    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr")))

    # Now inside iframe
    editor = wait.until(EC.visibility_of_element_located((By.ID, "tinymce")))

    # TinyMCE is a rich-text editor, not a normal input field.
    # Click it, select the existing text, then type the new text.
    editor.click()
    editor.send_keys(Keys.COMMAND + "a")
    editor.send_keys(Keys.BACKSPACE)
    editor.send_keys("Hello from Selenium inside iframe!")

    # Small pause so you can watch Selenium type inside the iframe before it exits.
    time.sleep(5)

    # Switch back to main page
    driver.switch_to.default_content()

    print("Done inside iframe")

finally:
    driver.quit()
