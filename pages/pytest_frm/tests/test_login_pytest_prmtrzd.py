import pytest

from pages.login_page import LoginPage

LOGIN_URL = "https://the-internet.herokuapp.com/login"


@pytest.mark.parametrize(
    "username,password,expected_message",
    [
        ("tomsmith", "SuperSecretPassword!", "You logged into a secure area!"),
        ("tomsmith", "wrongpass", "Your password is invalid!"),
        ("admin", "123", "Your username is invalid!"),
    ],
)
def test_login(driver, username, password, expected_message):
    driver.get(LOGIN_URL)

    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    assert expected_message in login_page.get_flash_message()

#Run without HTML report:
#./.venv/bin/python -m pytest pages/pytest_frm/tests/test_login_pytest_prmtrzd.py -v

#Run with HTML report:
#./.venv/bin/python -m pytest pages/pytest_frm/tests/test_login_pytest_prmtrzd.py -v --html=report.html
