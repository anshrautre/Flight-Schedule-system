import requests
import json
# Taking data from a api 
data=requests.get("https://api.aviationstack.com/v1/flights?access_key=7162db366e4bde54d49424573e2bae9e")
# converting api data in json format
data1=data.json()
# sorting json data for 
for d1 in data1["data"]:
        print(d1)
        print("*---------------------*")
        print("DEPARTED")
        print("*---------------------*")
        print(f"Flight Date : {d1["flight_date"]}")
        print(f"Flight departed Schedule : {d1["departure"]["scheduled"]}")
        print(f"Flight departed from : {d1["departure"]["airport"]}")
