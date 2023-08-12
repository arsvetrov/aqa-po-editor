import requests
from pprint import pprint
s = requests.Session()

url = 'https://po-editor-api.demo.p2h-cd.com/api/auth/registration/'
url1 = 'https://po-editor-api.demo.p2h-cd.com/api/auth/login/'

reg_data = {
    "email": "user1234@p2h.com",
    "password": "123456",
    #"name": "John Ivanov"
}

# Reg Call
# r = requests.post(url, json=reg_data)
# pprint(r.status_code)
# pprint(r.json())
print("*"*32)

# Login call

r = s.post(url1, reg_data)
token = r.json()["token"]
print(token)
print("*"*32)

# headers = {
#     'Authorization': token,
# }

url2 = "https://po-editor-api.demo.p2h-cd.com/api/applications"

j_data = {
  "name": "Cjhhangekkljndkj occupation123123",
  "description": "Change occupatjkion application",
  "domain": "https://chanlkge-cdcupajkjktioj.com",
  "platform": "lkQiwa"
}

response = s.post(url2, json=j_data, autorization=token)
print(response.status_code)
print(response.json())