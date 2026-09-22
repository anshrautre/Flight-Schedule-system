import requests
import json
# Taking data from a api 
data=requests.get("https://api.aviationstack.com/v1/flights?access_key=7162db366e4bde54d49424573e2bae9e")
# converting api data in json format
data1=data.json()
# sorting json data for 
for d1 in data1["data"]:
    if "Asia" in d1["departure"]["timezone"]:
        print(d1)
