import requests

payload = {
    "name": "Yufan QA",
    "username" : "yufantest@test.com"
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/users",
    json=payload
) 


print(response.status_code)

data = response.json()

print(data)