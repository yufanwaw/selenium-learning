from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/dropdown")

# Wait for dropdown
wait = WebDriverWait(driver, 10)
dropdown_element = wait.until(
    EC.presence_of_element_located((By.XPATH, "//select[@id='dropdown']"))
)

# Create Select object
dropdown = Select(dropdown_element)

# 🔹 Method 1: Select by visible text
#dropdown.select_by_visible_text("Option 1")

# 🔹 Method 2: Select by value
#dropdown.select_by_value("2")

# 🔹 Method 3: Select by index (starts from 0)
dropdown.select_by_index(2)

# Print selected option
selected = dropdown.first_selected_option.text
print("Selected option:", selected)
time.sleep(5)
driver.quit()