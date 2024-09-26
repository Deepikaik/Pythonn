class Account:
    def __init__(self):          #constructor
        print("Acc-CM")

    def deposit_amount(self,amount):                 #is instance
        print("Acc class-IM")
    
a1=Account()         #object is created
a1.deposit_amount(5000)    