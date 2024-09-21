import json

fp=open('data.json','r')

data=json.load(fp)
print(data)
print(type(data))
print(len(data))

