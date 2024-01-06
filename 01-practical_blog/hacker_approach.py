import requests
import json


# The API endpoint for the request.
url = "https://www.expedia.com/graphql"

# The payload (data) to be sent with the request, formatted as a JSON string.
# This includes various parameters like search criteria, dates, destination, etc.
payload = json.dumps({
  "variables": {
    "context": {
      "siteId": 1,
      "locale": "en_US",
      "eapid": 0,
      "currency": "USD",
      "device": {
        "type": "MOBILE_PHONE"
      },
      "identity": {
        "duaid": "8f5ed0c2-ceb2-4309-b1a6-5bed7c277edc",
        "expUserId": "-1",
        "tuid": "-1",
        "authState": "ANONYMOUS"
      },
      "privacyTrackingState": "CAN_TRACK",
      "debugContext": {
        "abacusOverrides": []
      }
    },
    "criteria": {
      "primary": {
        "dateRange": {
          "checkInDate": {
            "day": 12,
            "month": 1,
            "year": 2024
          },
          "checkOutDate": {
            "day": 14,
            "month": 1,
            "year": 2024
          }
        },
        "destination": {
          "regionName": "Dubai, Dubai, United Arab Emirates",
          "regionId": "6053839",
          "coordinates": None,
          "pinnedPropertyId": "1109595",
          "propertyIds": None,
          "mapBounds": None
        },
        "rooms": [
          {
            "adults": 2,
            "children": []
          }
        ]
      },
      "secondary": {
        "counts": [
          {
            "id": "resultsStartingIndex",
            "value": 3
          },
          {
            "id": "resultsSize",
            "value": 97
          }
        ],
        "booleans": [],
        "selections": [
          {
            "id": "sort",
            "value": "RECOMMENDED"
          },
          {
            "id": "guestRating",
            "value": "ANY"
          },
          {
            "id": "privacyTrackingState",
            "value": "CAN_TRACK"
          },
          {
            "id": "useRewards",
            "value": "SHOP_WITHOUT_POINTS"
          },
          {
            "id": "searchId",
            "value": "f2ce2dfc-2815-42eb-82db-50966d7efa21"
          }
        ],
        "ranges": []
      }
    },
    "destination": {
      "regionName": None,
      "regionId": None,
      "coordinates": None,
      "pinnedPropertyId": None,
      "propertyIds": None,
      "mapBounds": None
    },
    "shoppingContext": {
      "multiItem": None
    },
    "returnPropertyType": False,
    "includeDynamicMap": False
  },
  "operationName": "LodgingPwaPropertySearch",
  "extensions": {
    "persistedQuery": {
      "sha256Hash": "e4ffcd90dd44f01455f9ddd89228915a177f9ec674f0df0db442ea1b20f551c3",
      "version": 1
    }
  }
})
headers = {
  'authority': 'www.expedia.com',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'client-info': 'shopping-pwa,unknown,unknown',
  'content-type': 'application/json',
  'cookie': 'linfo=v.4,|0|0|255|1|0||||||||1033|0|0||0|0|0|-1|-1; CRQSS=e|0; CRQS=t|1`s|1`l|en_US`c|USD; currency=USD; iEAPID=0; tpid=v.1,1; MC1=GUID=8f5ed0c2ceb24309b1a65bed7c277edc; DUAID=8f5ed0c2-ceb2-4309-b1a6-5bed7c277edc; CRAS=network.cj.3273848.12639039.usr118CV0IOOLWAF1H772OBKVO59T-288175019; s_ppv=%5B%5BB%5D%5D; s_ips=1; s_ecid=MCMID%7C19615518666860970893864614561483805212; AMCVS_C00802BE5330A8350A490D4C%40AdobeOrg=1; eg_ppid=6f5e16a1-4e5b-4121-aed8-0d93e10c8fe4; session_id=6d6cf2ba-3131-4619-85fc-90991906be26; pageVisited=true; ttd_TDID=d5462844-ad22-4fcf-9a4b-991fa436eba3; eg_ppid=6f5e16a1-4e5b-4121-aed8-0d93e10c8fe4; EG_SESSIONTOKEN=dFwfU8nx-cLthlCfddDsC1ZuAH7iyukMA9YCbt4F6EgFHg:L3h5BIGRB2u83xgENe13SpwuuK2FDqgqtg4czXJg1cMfPyM6VqpML8qyIznsFBiH0NszunGcGvuZZUt7CJBlNA; _gcl_au=1.1.150857073.1704467111; _fbp=fb.1.1704467111352.1418899944; _gcl_aw=GCL.1704467112.EAIaIQobChMI8vv63sLGgwMV6QWiAx2h3weQEAAYASAAEgIQYfD_BwE; xdid=bdc165c8-ac49-48fa-80a9-1782e6370165|1704467120|expedia.com; OptanonConsent=isGpcEnabled=0&datestamp=Fri+Jan+05+2024+16%3A25%3A58+GMT%2B0100+(West+Africa+Standard+Time)&version=202305.1.0&browserGpcFlag=0&isIABGlobal=false&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CBG47%3A0%2CC0003%3A0%2CC0002%3A0%2CC0004%3A0&AwaitingReconsent=false; SheetBannerClose=yes; s_fid=7E966AF4ED090006-1F68B3D244A81058; page_name=page.Hotel-Search; HMS=e69a0b15-aa1f-408e-a436-204df3ea40b9; _abck=534B58F2F9BCBD44ADC2ADFCE5E0267B~-1~YAAQFbU+F7YFe2+MAQAAOdtH3Qv06u63MrQq2Y3VOX3N2MEQZHjZ+cxXThDL4nbJxw6fJwFRmYcgj4rkcN0LBN4vF4glxot6Hmq1bQ/1NQYJRKZ9osG/r8EjVdQglh4h6TD4qg/j6tz1WoX3x19nIRWuyQb/Ly0yR+h9xqYZL3K39vV+qPtnFgALzgbnnZ2B8KVtG3mbwBElafWB5QMs2y2rF1x4dL8dIQEyiMrkjgAPctKa7YYMUHxFZFqD0GsTNqXIZxYiXabrG0oZI0+oa52Z1MDYstOt82Uv63qTsHQWGTZSWQHFISoGFQoDgqwiCe0V+7xq/2OUSEflqywJIW1SLVCqx7IJaAb4XooxiieQ7xGrUORarpjwgZ2EUqyNpZJfgept4MfYp7A=~-1~-1~-1; bm_sz=BEB8FCFF96260580F6F47F8FACACDEF5~YAAQFbU+F7kFe2+MAQAAOdtH3Rb286zupxKH0FEnFO3OUufamQFVZqchRmjSRNkbxnS268VOHHiT4BQLvYlpW6evuVNf6iytJXByeULeKei+mF7qfmydSDrXTH9vy9kxIx+tvRQYrOmrMPgA54BA/+HfW7EBicEsDyP3sQLxGU6kO7Mq7vu0DK0Dpo9QlUlVFA9boegrxdrDl5dRpZGeyoFu/doSqpeIYECPZDBMI4AS1nGIovFDai+K7aAss5oduqyCe5m7VoA70Bu9RwUFpBmvrviX6izNftv2UdXNtDwYe8Ue~3687735~3490608; s_ppn=page.Hotel-Search; AWSELB=D79B53F10ADCF9DDDF09C7B84896C09A6222EC2F5D58CCE84F5EE42C490A9D04E32FD396848109F621500631FA6FB5BBC593F2679DD5B43C13A5FFB39FBA33527A4DDDAFE1; AWSELBCORS=D79B53F10ADCF9DDDF09C7B84896C09A6222EC2F5D58CCE84F5EE42C490A9D04E32FD396848109F621500631FA6FB5BBC593F2679DD5B43C13A5FFB39FBA33527A4DDDAFE1; AMCV_C00802BE5330A8350A490D4C%40AdobeOrg=1585540135%7CMCIDTS%7C19728%7CMCMID%7C19615518666860970893864614561483805212%7CMCAID%7CNONE%7CMCOPTOUT-1704526737s%7CNONE%7CMCAAMLH-1705124337%7C6%7CMCAAMB-1705124337%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CvVersion%7C4.4.0; _uetsid=d2b97db0abdb11ee8a59e38e1abb495f; _uetvid=d2b9c560abdb11eeba6557616bab4011; bm_mi=D910399823452E7895D3171A24E020BD~YAAQFbU+F4Aae2+MAQAA5zdK3RYloo8VtH3Ywn3hemy6wn9XLsf4dbiQPyrgZlAHYcuni1zjTJi/ymsDlWy0ZehwiyLqDKzN3wDdgdlAlZYfd7RxBJlijf51r3F2t1KoPU/Hhv9d38FQdjLJNnsBnbg6hzoqTR/0K7ke3SHLArpLh8SsutBr7YP/2ZbnSFhJxu7FKMZ5/SR8UNDPXESuz6xgV9CcHLOfuWJoCaZsIFcexMiKp9f/Gcm1VKDlrza2LG9sYHxhvjzG2EeXSxwryo5HOktnTXJTcWshxFDBp+xZY1Rgf33eNNC4WH2ytkTW6ewLbl4ORG7STR/FxMdxNVascJu13HT3ZyJaDh/Q7FvwZp5WMPxne+QRjHIAHQ==~1; bm_sv=B8E20A3FC3494482DF40C7D01D5067FA~YAAQFbU+F4Mae2+MAQAAADhK3RaofB9qU5JskJaRrnXxVQkO6Vg61ZdhifPK7XCI9MfhMLcwa14YHgo8PFro6Ki20x4ixUPcXapRjiKjdqOSHsxB2E7sgWdJepe4LAtrAsihXWi+YilMFg/6M0GZBuXxhU3GO2oRQYrq3EvNbKqPzJmv/qsLQLoZKHkprRTZrBeMz8K/W1vZVXpBYlRXYQyZfQbxtG8lMBu8FSiFnxM5TGDrYzAZKo9M7F6TVAZ4SeU=~1; ak_bmsc=D352A9542B8883E65E0EFD3505E60EA1~000000000000000000000000000000~YAAQFbU+F7Yge2+MAQAAuLNK3Ra2+1rcul+2IeoB9sVQvBBNjhVFoSTIl4XdVYIiHyVxFLSdb4WOMEq0wjbqnGINtJKnjlaVUVOsVF5KhGcZiQqLJmry+eluZUIINqFLSR5xoyImNpnnR5oyZLe0qpyOaDuKGp+YjifsaZiiP4RQ4xqg0TSsu6iSBfJLRDUKwXBu6DB7HgM6AAXVLvIwmtHsi3C8EVV3SH2YRMpYjc9CSw2MddRr/P26YfwirRsKyELE7qrcDzbtgQB1dIsko44l5Rc3lhpGWP15u30z58GaoDMa2Cjyt6wiU5dHF6iyDoMJY2uNa5rLLPoofaMogQJ+x4iEfRs6o/Tk8+s6yR0A6qYLuW72dsZbEj5k2R3HtlXa0jDSma/KfugjCGcLrSQaX6EUAsHNJsH4QhEpxEULxqxEH+24FRHyrY++LZZZzgPU63aKyRFX40NYeW7xqdKNbDg1NssnqnRn1oQCQyeC9bWe1kfLaBOebcVSdsGJT+M+NB1pzD7yGQiVFm5oudySvEle/B0H83JAg8HSPRyv63SlgTUWshYqSkr6U7uEsmwoVEAMkrcLHWeu5m7ZXdT0JjBl+S+D4H0qw46Rng==; __gads=ID=09cfa52cb1455b0f:T=1704467111:RT=1704519920:S=ALNI_MYv1uqC4Bv6oSYWRdXY6Vb8eL9SOw; __gpi=UID=00000cef355f3c9e:T=1704467111:RT=1704519920:S=ALNI_MZ8igGRl6YQvV3PcyxXOhWRQ41lag; s_tp=25254; JSESSIONID=2B38072E242E6F1383AC9AD23E1889ED; cesc=%7B%22aff%22%3A%5B%22AFF.network.cj.3273848.12639039.usr118CV0IOOLWAF1H772OBKVO59T-288175019%22%2C1704519644668%5D%2C%22lpe%22%3A%5B%22cf4329e1-757a-432b-9e6e-528ea708d2d7%22%2C1704520019888%5D%2C%22gclid%22%3A%5B%22EAIaIQobChMI8vv63sLGgwMV6QWiAx2h3weQEAAYASAAEgIQYfD_BwE%22%2C1704519644668%5D%2C%22marketingClick%22%3A%5B%22false%22%2C1704520019888%5D%2C%22lmc%22%3A%5B%22AFF.NETWORK.CJ.3273848.12639039.USR118CV0IOOLWAF1H772OBKVO59T-288175019%22%2C1704520019888%5D%2C%22hitNumber%22%3A%5B%2214%22%2C1704520019887%5D%2C%22amc%22%3A%5B%22AFF.NETWORK.CJ.3273848.12639039.USR118CV0IOOLWAF1H772OBKVO59T-288175019%22%2C1704520019888%5D%2C%22visitNumber%22%3A%5B%222%22%2C1704519522946%5D%2C%22ape%22%3A%5B%22cf4329e1-757a-432b-9e6e-528ea708d2d7%22%2C1704520019888%5D%2C%22cidVisit%22%3A%5B%22AFF.network.cj.3273848.12639039.usr118CV0IOOLWAF1H772OBKVO59T-288175019%22%2C1704520019888%5D%2C%22entryPage%22%3A%5B%22page.Hotel-Search%22%2C1704520019888%5D%2C%22cid%22%3A%5B%22AFF.network.cj.3273848.12639039.usr118CV0IOOLWAF1H772OBKVO59T-288175019%22%2C1704519644668%5D%7D; _dd_s=rum=0&expire=1704520922748; DUAID=8f5ed0c2-ceb2-4309-b1a6-5bed7c277edc; HMS=e69a0b15-aa1f-408e-a436-204df3ea40b9; MC1=GUID=8f5ed0c2ceb24309b1a65bed7c277edc; cesc=%7B%22aff%22%3A%5B%22AFF.network.cj.3273848.12639039.usr118CV0IOOLWAF1H772OBKVO59T-288175019%22%2C1704519644668%5D%2C%22lpe%22%3A%5B%22cf4329e1-757a-432b-9e6e-528ea708d2d7%22%2C1704520686978%5D%2C%22gclid%22%3A%5B%22EAIaIQobChMI8vv63sLGgwMV6QWiAx2h3weQEAAYASAAEgIQYfD_BwE%22%2C1704519644668%5D%2C%22marketingClick%22%3A%5B%22false%22%2C1704520686978%5D%2C%22lmc%22%3A%5B%22AFF.NETWORK.CJ.3273848.12639039.USR118CV0IOOLWAF1H772OBKVO59T-288175019%22%2C1704520686978%5D%2C%22hitNumber%22%3A%5B%2215%22%2C1704520686978%5D%2C%22amc%22%3A%5B%22AFF.NETWORK.CJ.3273848.12639039.USR118CV0IOOLWAF1H772OBKVO59T-288175019%22%2C1704520686978%5D%2C%22visitNumber%22%3A%5B%222%22%2C1704519522946%5D%2C%22ape%22%3A%5B%22cf4329e1-757a-432b-9e6e-528ea708d2d7%22%2C1704520686978%5D%2C%22cidVisit%22%3A%5B%22AFF.network.cj.3273848.12639039.usr118CV0IOOLWAF1H772OBKVO59T-288175019%22%2C1704520686978%5D%2C%22entryPage%22%3A%5B%22page.Hotel-Search%22%2C1704520686978%5D%2C%22cid%22%3A%5B%22AFF.network.cj.3273848.12639039.usr118CV0IOOLWAF1H772OBKVO59T-288175019%22%2C1704519644668%5D%7D',
  'origin': 'https://www.expedia.com',
  'referer': 'https://www.expedia.com/Hotel-Search?adults=&children=&destination=Dubai%2C%20Dubai%2C%20United%20Arab%20Emirates&endDate=2024-01-14&guestRating=ANY&regionId=6053839&selected=1109595&semdtl=&sort=RECOMMENDED&startDate=2024-01-12&theme=&useRewards=false&userIntent=',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
  'x-enable-apq': 'true',
  'x-page-id': 'page.Hotel-Search,H,20'
}

response = requests.request("POST", url, headers=headers, data=payload)


# Checking if the request was successful
if response.status_code == 200:
    # Printing the JSON data
    print(response.json())
else:
    print(f"Failed to retrieve data: {response.status_code}")
