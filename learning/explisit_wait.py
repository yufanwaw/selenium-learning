from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

wait = WebDriverWait(driver, 10)

# Click start button
start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
start_button.click()

# Wait until text appears
finish_text = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "#finish h4"))
)

print("Result:", finish_text.text)

driver.quit()