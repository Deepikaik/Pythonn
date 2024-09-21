'''fp=open('data.txt','r')    #fp-file pointer
data=fp.read()
print(data)'''
#=================================================
fp1=open('data.txt','r')
data=fp1.read()

fp2=open('hello.txt','w')
fp2.write(data)
print('new file created')      #the data from data.txt will override the data from hello.txt
fp1.close()
fp2.close()

#=================================================
fp1=open('data.txt','r')     #read 
data=fp1.read()

fp2=open('bengaluru.txt','w')   #write
fp2.write(data)

fp3=open('city.txt','a')     #append
fp3.write(data)


print('new file created')     #ne file is created by default if not initiated
fp1.close()
fp2.close()
fp3.close()