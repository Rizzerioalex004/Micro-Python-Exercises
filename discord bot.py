import urequests as requests 
import ujson as json


url1 = "https://discord.com/api/webhooks/890522840821006366/Ol38KeLTe2aXel4y2ECnDLuiDdilNYiEjrhMYHTKp8FsGyVPn6CFHD5HwM-7nCR8ww0B"
url2 = "https://discord.com/api/webhooks/890543506731446273/ShZkMwZ-fMwA7egdOuGxueSKJyByw204Vt0gYkLkL5xu2TYtEvBiwEMh2ZpKQcNGtAdC"

headers = {
    'Content-Type': 'application/json'
}
while True:
    payload = json.dumps({
        "content": input("Enter any msg: "),
        "username": input("Enter username: "),
        "avatar_url": input("Paste avatar url: ")
        })
    response = requests.post(url1, headers=headers, data=payload)

    print(response.json)