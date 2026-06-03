from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page_exc1 import LoginPage
from pages.secure_page_exc1 import SecurePage


def test_login_page(driver):
    driver.get("https://the-internet.herokuapp.com/login")
    login_page = LoginPage(driver)

    login_page.enter_username("tomsmith")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_login()

    message = login_page.get_flash_msg()
    assert "You logged into a secure area!" in message

    secure_page = SecurePage(driver)
    secure_page.click_logout()

    message = WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element(
            (By.ID, "flash"),
            "You logged out of the secure area!"
        )
    )
    assert message

    assert login_page.is_username_visible()
    assert login_page.is_password_visible()
