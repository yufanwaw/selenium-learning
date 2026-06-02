from selenium import webdriver
from selenium.webdriver.common.by import By
import ollama

def ai_find_element(driver, description):
    html = driver.page_source[:4000]

    response = ollama.chat(
        model="llama3",
        messages=[{
            "role": "user",
            "content": f"""Given this HTML, return ONLY a Python tuple like:
("XPATH", "//button[@id='login']")
or ("CSS_SELECTOR", ".submit-btn")

Find: {description}

HTML:
{html}"""
        }]
    )

    raw = response["message"]["content"].strip()
    by_type, selector = eval(raw)

    by_map = {
        "XPATH": By.XPATH,
        "CSS_SELECTOR": By.CSS_SELECTOR,
        "ID": By.ID,
        "NAME": By.NAME,
        "LINK_TEXT": By.LINK_TEXT,
    }
    return driver.find_element(by_map[by_type], selector)


# --- Main script starts here ---
driver = webdriver.Chrome()
driver.get("https://quotes.toscrape.com")

quote = ai_find_element(driver, "the first quote text on the page")
print("Found:", quote.text)

driver.quit()