'''fp=open("one.txt",'r')   #error occurs filenot found
data=fp.read()     

print(data)
print('gm')'''


try:
    fp=open("one.txt",'r')
except:
    fp=open("data.txt",'r')
    data= fp.read()
    print(data)