import requests


#Challenge 1: get users API 
print("Challenge 1: get users API")
response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    timeout=10,
)

assert response.status_code == 200

users = response.json()

for user in users:
    print(user["name"])

print("End of Challenge 1")


#Challenge 2: Verify total users = 10
print("Challenge 2: Verify total users = 10")
response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    timeout=10,
)

assert response.status_code == 200

users = response.json()
print("Total Users:",len(users))

print("End of Challenge 2")


#Challenge 3: Print All Emails
print("Challenge 3: Print All Emails")
response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    timeout=10,
)

assert response.status_code == 200

users = response.json()
for user in users:
    print(user["email"])

print("End of Challenge 3")


#Challenge 4: Validate one username exist
print("Challenge 4: Validate one username exist")
response = requests.get(
    "https://jsonplaceholder.typicode.com/users",
    timeout=10,
)

assert response.status_code == 200

users = response.json()
expected_name = "Clementina DuBuque"
names = [user["name"] for user in users]

assert expected_name in names
print("It's Found")

print("End of Challenge 4")


