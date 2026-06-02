from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


URL = "https://the-internet.herokuapp.com/windows"
TIMEOUT = 10


def main():
    # Create the Chrome driver. webdriver_manager downloads/uses the correct
    # ChromeDriver version for the Chrome browser installed on your machine.
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # WebDriverWait lets Selenium wait for a condition instead of using
    # time.sleep(). This makes the script faster and more stable.
    wait = WebDriverWait(driver, TIMEOUT)

    try:
        # Open the test page that contains a link which launches a new window/tab.
        driver.get(URL)

        # Save the first window handle so we can switch back to it later.
        main_window = driver.current_window_handle
        print("Main window:", main_window)

        # Click the link that opens another browser window/tab.
        driver.find_element(By.LINK_TEXT, "Click Here").click()

        # Wait until Selenium can see both the original window and the new one.
        wait.until(EC.number_of_windows_to_be(2))

        # Get every open window handle. Selenium uses these IDs to switch tabs.
        all_windows = driver.window_handles
        print("All windows:", all_windows)

        # Find the handle that is not the original window, then switch to it.
        new_window = next(
            window for window in all_windows if window != main_window
        )
        driver.switch_to.window(new_window)

        # Wait until the heading appears in the new tab before reading its text.
        heading = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".example h3"))
        )
        print("New tab title:", driver.title)
        print("The text inside the new tab is:", heading.text)

        # Switch Selenium's focus back to the original window.
        driver.switch_to.window(main_window)
        print("Back to main title:", driver.title)

    finally:
        # Always close the browser, even if the script fails before the end.
        driver.quit()


# This makes the file runnable directly with: python3 new_windows_or_tabs.py
if __name__ == "__main__":
    main()
