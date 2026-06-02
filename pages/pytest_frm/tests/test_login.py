from pathlib import Path

from pages.login_page import LoginPage
from pages.secure_page import SecurePage

SCREENSHOTS_DIR = Path("screenshots")


def test_valid_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    login_page = LoginPage(driver)
    login_page.enter_username("tomsmith")
    login_page.enter_password("SuperSecretPassword!")
    login_page.click_login()
    assert "secure area" in login_page.get_flash_message()

    secure_page = SecurePage(driver)
    secure_page.click_logout()


def test_login_with_incorrect_password(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    login_page = LoginPage(driver)
    login_page.enter_username("tomsmith")
    login_page.enter_password("WrongSuperSecretPassword!")
    login_page.click_login()
    # assert "Your password is invalid!" in login_page.get_flash_message()

    try:
        assert "Your password is invalid!" in login_page.get_flash_message()

    except AssertionError as e:
        SCREENSHOTS_DIR.mkdir(exist_ok=True)
        driver.save_screenshot(str(SCREENSHOTS_DIR / "test_login_with_incorrect_password.png"))
        print("Test failed:", e)
        raise


#./.venv/bin/python -m pytest pages/pytest_frm/tests/test_login.py --html=report.html
#
