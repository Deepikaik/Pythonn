import csv

fp=open('data.csv','r')
rows=csv.reader(fp)  

users=list(rows)

for user in users:
    print(user)

