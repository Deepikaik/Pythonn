import json

fp1=open('data.json','r')
users=json.load(fp1)   #from json to py
print(users)

maleUsers=list(filter(lambda user:user['gender']=='Male',users))
femaleUsers=list(filter(lambda user:user['gender']=='Female',users))

fp2=open('male.json','w')
json.dump(maleUsers,fp2)  #from py to js
print(len(maleUsers))

fp3=open('female.json','w')
json.dump(femaleUsers,fp3)
print(len(femaleUsers))

