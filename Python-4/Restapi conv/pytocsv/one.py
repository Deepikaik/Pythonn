import csv

customers= [{'id':'101','name':'Rahul','avail':True},
          {'id':'102','name':'sonia','avail': False},
          {'id':'103','name':'Priya','avail':True}]

fp1=open('emp.csv','w')
wr=csv.writer(fp1)
wr.writerow(['id','name','avail'])
for cust in customers:
    wr.writerow([cust['id'],cust['name'],cust['avail']])

    print(cust)

fp1.close()

