class Account:
    min_Bal=500

    def open_Account(self):            #self is a key word   self is instance method
        print('account is open')      #no need of decorator because of #instance method
    
    @classmethod
    def m2(cls):
        pass

    @staticmethod
    def m3():
        pass

a1=Account()
a2=Account()
a3=Account()

print(a1)
print(a2)

print(a3)
print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)

print(Account.__dict__)
    