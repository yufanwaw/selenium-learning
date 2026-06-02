import json

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

USERS_API = "https://jsonplaceholder.typicode.com/users"


def print_section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


payload = {
    "name": "Yufan QA",
    "username": "yufantest@test.com",
}

print_section("Create User via API")
response = requests.post(USERS_API, json=payload, timeout=10)

print("Status Code:", response.status_code)
created_user = response.json()
print(json.dumps(created_user, indent=4))

assert response.status_code == 201
assert created_user["name"] == payload["name"]
assert created_user["username"] == payload["username"]

print_section("Open Users Page in Browser")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    driver.get(USERS_API)

    print("Browser Title:", driver.title)
    print("Current URL:", driver.current_url)
    print(
        "\nNote: JSONPlaceholder is a fake API. "
        "POST returns a created user, but it does not permanently save it "
        "into the /users list."
    )

finally:
    driver.quit()


