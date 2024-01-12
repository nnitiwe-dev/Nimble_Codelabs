import requests
import json

with open('secrets/config.json', 'r') as keys:
    secret_keys = json.load(keys)

url = "https://api.webit.live/api/v1/async/web"

payload = json.dumps({
  "url": "https://www.expedia.com/Hotel-Search?adults=&children=&destination=Dubai%2C%20Dubai%2C%20United%20Arab%20Emirates&endDate=2024-01-14&guestRating=ANY&regionId=6053839&selected=1109595&semdtl=&sort=RECOMMENDED&startDate=2024-01-12&theme=&useRewards=false&userIntent=",
  "method": "GET",
  "parse": True,
  "render": True,
  "parse_options": {
    "source": "parsit-ai",
    "params": {
      "schema": {
        "fields": {
          "hotel_name": {
            "type": "str"
          },
          "hotel_location": {
            "type": "str"
          },
          "images_urls": {
            "type": "str"
          },
          "price": {
            "type": "str"
          },
          "total_price": {
            "type": "str"
          },
          "hotel_reviews": {
            "type": "str"
          }
        }
      }
    }
  }
})
headers = {
  'Authorization': secret_keys['key'],
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
