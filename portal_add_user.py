import requests

def create_unix_user(userPass, userId):
    url = 'http://127.0.0.1:8080/api/add_unix_user/'
    payload = {'userPass': userPass, 'userId': userId}
    response = requests.post(url, data=payload)
    data = response.json()
    return data

userPass = "password"
userId = "user123"
result = create_unix_user(userPass, userId)
print(result)
