import json

fp1=open('data.json','r')
users=json.load(fp1)

employees=[]
for user in users:
    employees.append({'eid':user['id'],
    'ename':user['name'],
    'email':user['email']})
    
fp2=open('emp.json','w')
json.dump(employees,fp2)

print(employees)
fp1.close()
fp2.close()