import requests
import json

with open('secrets/config.json', 'r') as keys:
    secret_keys = json.load(keys)
    
url = "https://api.webit.live/api/v1/realtime/web"

payload = json.dumps({
  "url": "https://www.expedia.com/Hotel-Search?adults=&children=&destination=Dubai%2C%20Dubai%2C%20United%20Arab%20Emirates&endDate=2024-01-14&guestRating=ANY&regionId=6053839&selected=1109595&semdtl=&sort=RECOMMENDED&startDate=2024-01-12&theme=&useRewards=false&userIntent=",
  "parse": True,
  "format": "json",
  "render": True,
  "country": "US",
  "locale": "en",
  "render_flow": [
    {
      "wait": {
        "delay": 8000
      }
    }
  ],
  "network_capture": [
    {
      "url": {
        "type": "contains",
        "value": "www.expedia.com/graphql"
      }
    }
  ]
})



headers = {
  'Content-Type': 'application/json',
  'Authorization': secret_keys['key']
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
