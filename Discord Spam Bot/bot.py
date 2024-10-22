import requests

url = 'https://discord.com/api/webhooks/791468052465713183/6dqXkEkBDu116lVi-PYV1Lnakx0_fZSStqaZIEyLzX_L1mi0ReL5V5mmBGMnauP9JuW5'
import json

data = {
    "content": "@Realer"
}

count = 0
amount = 1000000000

while count < amount:
    r = requests.post(url, data=data)
    print(r.ok)
    count += 1



