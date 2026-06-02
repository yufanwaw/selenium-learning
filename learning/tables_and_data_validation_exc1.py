from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://the-internet.herokuapp.com/tables")

wait = WebDriverWait(driver, 10)

rows = driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr")

for row in rows:
    print("found:",row.text)


driver.quit()

