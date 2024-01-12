import requests
import json

with open('secrets/config.json', 'r') as keys:
    secret_keys = json.load(keys)

result_download_url = "https://api.webit.live/api/v1/tasks/4c9f40b5-86ce-4d6f-bedf-64e3576f2503/results"

payload = {}
headers = {
  'Authorization': secret_keys['key'],
  'Content-Type': 'application/json'
}

response = requests.request("GET", result_download_url, headers=headers, data=payload)

print(response.text)
