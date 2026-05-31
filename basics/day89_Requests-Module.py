'''
Requests Module hota hein HTTP Requests Maarney ke liye

Agar aap Practically istemaal karna chahtey ho Python ko to Requests Module ka istemall Karsaktey ho
'''

import requests
# response = requests.get("https://www.google.com")
# print(response.text)
# Mujhey Sab Text HTML Ke Form Mil gaya , aur agar main chahun to is HTML ko Parse bhi karsakta hun

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Sadiq",
    "body": "bai",
    "userId": 12
}

headers = {
    "content-type":"application/json; charset=UTF-8"
}
response1 = requests.post(url, headers=headers,json=data)
print(response1.text)
