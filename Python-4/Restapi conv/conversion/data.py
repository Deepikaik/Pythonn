import json
import csv

customers= [{'id':'101','name':'Rahul','avail':True},
          {'id':'102','name':'sonia','avail': False},
          {'id':'103','name':'Priya','avail':True}
]

fp1=open('emp.json','w')
fp2=open('emp.csv','w')

json.dump(customers,fp1)
print('json file created')

fp1.close()
fp2.close()