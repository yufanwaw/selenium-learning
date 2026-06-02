import time
from pathlib import Path

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


URL = "https://demoqa.com/select-menu"
TIMEOUT = 30


def get_chromedriver_service():
    """Use a cached ChromeDriver first, then fall back to webdriver_manager."""
    cached_drivers = sorted(
        Path.home().glob(".wdm/drivers/chromedriver/mac64/*/chromedriver-*/*")
    )

    for driver_path in reversed(cached_drivers):
        if driver_path.name == "chromedriver":
            return Service(str(driver_path))

    return Service(ChromeDriverManager().install())


def select_react_option(wait, input_id, option_text):
    """Select one option from a React dropdown by typing and pressing Enter."""
    dropdown_input = wait.until(EC.element_to_be_clickable((By.ID, input_id)))
    dropdown_input.location_once_scrolled_into_view
    dropdown_input.click()
    dropdown_input.send_keys(option_text)
    dropdown_input.send_keys(Keys.ENTER)
    return option_text


def select_react_multi_options(wait, input_id, option_texts):
    """Select multiple options from a React multi-select dropdown."""
    for option_text in option_texts:
        dropdown_input = wait.until(EC.element_to_be_clickable((By.ID, input_id)))
        dropdown_input.location_once_scrolled_into_view
        dropdown_input.click()
        dropdown_input.send_keys(option_text)
        dropdown_input.send_keys(Keys.ENTER)

    return option_texts


def main():
    # Use the cached ChromeDriver so Selenium Manager does not hang at startup.
    options = Options()
    options.page_load_strategy = "eager"
    options.add_argument("--blink-settings=imagesEnabled=false")

    service = get_chromedriver_service()
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_page_load_timeout(20)
    wait = WebDriverWait(driver, TIMEOUT)

    try:
        print("Opening DemoQA select menu page...", flush=True)
        driver.maximize_window()
        try:
            driver.get(URL)
        except TimeoutException:
            print("Page load timed out, continuing with visible page...", flush=True)

        # Hide ad containers that can cover elements while practicing Selenium.
        driver.execute_script(
            """
            const selectors = ['#fixedban', 'iframe[id^="google_ads"]'];
            selectors.forEach((selector) => {
                document.querySelectorAll(selector).forEach((element) => {
                    element.style.display = 'none';
                });
            });
            """
        )

        # First dropdown: "Select Value" custom React dropdown.
        selected_value = select_react_option(
            wait, "react-select-2-input", "Group 1, option 1"
        )

        # Second dropdown: "Select One" custom React dropdown.
        selected_one = select_react_option(wait, "react-select-3-input", "Dr.")

        # Third dropdown: "Old Style Select Menu" normal HTML select dropdown.
        old_style_element = wait.until(
            EC.element_to_be_clickable((By.ID, "oldSelectMenu"))
        )
        old_style_element.location_once_scrolled_into_view
        old_style_dropdown = Select(old_style_element)
        old_style_dropdown.select_by_visible_text("Purple")
        selected_old_style = old_style_dropdown.first_selected_option.text

        # Multiple dropdown: "Multiselect drop down" custom React dropdown.
        selected_multi_dropdown = select_react_multi_options(
            wait, "react-select-4-input", ["Green", "Blue"]
        )

        # Standard multi-select list: select at least two options from the list.
        cars_element = wait.until(EC.element_to_be_clickable((By.ID, "cars")))
        cars_element.location_once_scrolled_into_view
        cars_dropdown = Select(cars_element)
        cars_dropdown.select_by_visible_text("Volvo")
        cars_dropdown.select_by_visible_text("Audi")
        selected_cars = [
            option.text for option in cars_dropdown.all_selected_options
        ]

        print("Selected value dropdown:", selected_value)
        print("Selected one dropdown:", selected_one)
        print("Selected old style dropdown:", selected_old_style)
        print("Selected multi dropdown:", selected_multi_dropdown)
        print("Selected standard multi-select:", selected_cars)

        # Small pause so you can see the selected dropdown values before Chrome closes.
        time.sleep(5)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
