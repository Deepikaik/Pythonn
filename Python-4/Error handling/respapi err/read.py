import requests
import json
import csv

api_url= 'https://jsonplaceholder.typicode.com/users'
user_data= None
try:
    user_data=requests.get(api_url)
    users=user_data.json()
    user_data.raise_for_status()
except requests.exceptions.RequestException as e:
    fp=open('data.json','r')
    users=json.load(fp)
    print(users)