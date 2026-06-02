import sys
from pathlib import Path

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from pages.login_page import LoginPage
from pages.secure_page import SecurePage


def test_valid_login():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        driver.get("https://the-internet.herokuapp.com/login")

        login_page = LoginPage(driver)

        login_page.enter_username("tomsmith")
        login_page.enter_password("SuperSecretPassword!")
        login_page.click_login()

        message = login_page.get_flash_message()

        assert "You logged into a secure area!" in message

        secure_page =SecurePage(driver)
        secure_page.click_logout()

        assert "/login" in driver.current_url
        assert "You logged out of the secure area!" in login_page.get_flash_message()
        assert login_page.is_username_visible()
        assert login_page.is_password_visible()
        print("Sucess!")

    finally:
        driver.quit()


if __name__ == "__main__":
    test_valid_login()
