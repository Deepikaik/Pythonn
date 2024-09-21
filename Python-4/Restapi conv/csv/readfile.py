import csv

fp=open('data.csv','r')
rows=csv.reader(fp)            #reader() used to read the fp

print(rows)
print(type(rows))
for row in rows:
    print(row)