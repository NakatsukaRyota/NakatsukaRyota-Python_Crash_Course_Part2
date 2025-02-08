import json

import requests

url = "https://hacker-news.firebaseio.com/v0/item/31353677.json"
r = requests.get(url)
print(f"ステータスコード: {r.status_code}")

response_dict = r.json()
response_string = json.dumps(response_dict, indent=4)
print(response_string)
