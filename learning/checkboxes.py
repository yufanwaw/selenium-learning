from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/checkboxes")

# Wait until checkboxes are present
wait = WebDriverWait(driver, 10)
checkboxes = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#checkboxes input[type='checkbox']"))
)

# Safety check
if len(checkboxes) < 2:
    print("❌ Expected 2 checkboxes, but found:", len(checkboxes))
    driver.quit()
    exit()

# Function to print state
def print_state(stage):
    print(f"\n{stage}:")
    print("Checkbox 1:", checkboxes[0].is_selected())
    print("Checkbox 2:", checkboxes[1].is_selected())

# Before state
print_state("Before")

# Ensure first checkbox is checked
if not checkboxes[0].is_selected():
    checkboxes[0].click()

# Ensure second checkbox is unchecked
if checkboxes[1].is_selected():
    checkboxes[1].click()

# After state
print_state("After")

driver.quit()