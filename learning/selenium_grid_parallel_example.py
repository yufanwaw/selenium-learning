from concurrent.futures import ThreadPoolExecutor, as_completed

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

GRID_URL = "http://localhost:4444/wd/hub"
LOGIN_URL = "https://the-internet.herokuapp.com/login"


def create_options(browser_name):
    """Create browser options for Selenium Grid."""
    if browser_name == "chrome":
        return webdriver.ChromeOptions()

    if browser_name == "firefox":
        return webdriver.FirefoxOptions()

    raise ValueError(f"Unsupported browser: {browser_name}")


def run_login_test(browser_name):
    """Run one login test session on Selenium Grid."""
    options = create_options(browser_name)
    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options,
    )

    try:
        wait = WebDriverWait(driver, 10)
        driver.get(LOGIN_URL)

        wait.until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(
            "tomsmith"
        )
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        flash_message = wait.until(
            EC.visibility_of_element_located((By.ID, "flash"))
        ).text

        assert "You logged into a secure area!" in flash_message
        return f"{browser_name}: PASSED"

    except Exception as error:
        return f"{browser_name}: FAILED - {error}"

    finally:
        driver.quit()


if __name__ == "__main__":
    browsers = ["chrome", "firefox"]
    #browsers = ["chrome"]

    # Each browser runs in its own thread.
    # Selenium Grid receives both sessions and distributes them to available nodes.
    with ThreadPoolExecutor(max_workers=len(browsers)) as executor:
        futures = [
            executor.submit(run_login_test, browser_name)
            for browser_name in browsers
        ]

        for future in as_completed(futures):
            print(future.result())


# How to run Selenium Grid locally with Docker:
# docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome:latest
#
# If you use standalone Chrome only, change:
# browsers = ["chrome", "firefox"]
# to:
# browsers = ["chrome"]
#
# For Chrome + Firefox parallel testing, use docker compose with selenium hub/nodes,
# or run a Grid image/config that has both browser nodes available.
#
# Run this file:
# ./.venv/bin/python learning/selenium_grid_parallel_example.py


#cd /Users/yufannico/Documents/selenium
#docker compose up -d
#./.venv/bin/python learning/selenium_grid_parallel_example.py
#docker compose down
