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


#rows = driver.find_elements(By.CSS_SELECTOR, "#table1 tbody tr")
#print("Total Rows: ",len(rows))

#for row in rows:
#    print(row.text)

#cell = driver.find_element(By.XPATH,"//table[@id='table1']/tbody/tr[1]/td[2]")
#print(cell.text)

#find specific data in cell
#rows = driver.find_elements(By.CSS_SELECTOR,"#table1 tbody tr")
#for row in rows:
#    if "Jason" in row.text:
#        print("Found", row.text)


#Print all data from col 1
#col1 = driver.find_elements(By.XPATH,"//table[@id='table1']/tbody/tr/td[1]")
#for row in col1:
#    print(row.text)

rows = driver.find_elements(By.XPATH,"//table[@id='table1']/thead/tr")
for row in rows:
    if "Due" in row.text:
        print("Found",row.text)

driver.quit()

