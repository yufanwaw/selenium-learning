import requests

payload = {
    "username": "emilys",
    "password": "emilyspass"
}

response = requests.post(
    "https://dummyjson.com/auth/login",
    json=payload
)

print(response.status_code)

data = response.json()

print(data)



token = data["accessToken"]

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(
    "https://dummyjson.com/auth/me",
    headers=headers
)

print(response.status_code)
print(response.json())