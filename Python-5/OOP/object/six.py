class Account:
    acc_Bal=0
    def deposit_amount(Self,amount):     #to refer to class members within the class self is used
        Self.acc_Bal=Self.acc_Bal+amount


a1=Account()
a2=Account()

print(a1.__dict__)
print(a2.__dict__)

a1.deposit_amount(1000)
a2.deposit_amount(5000)

print(a1.__dict__)
print(a2.__dict__)