class Account:
    def open_acc(self):
        print("acc opned successfully")

    def deposit(self):
        print("amount deposited")

    def withdrawl(self):
        print("amount withdrawn")

    def get_bal(self):
        print("low bal")

a1=Account()
a1.open_acc()
a1.deposit(5000)
a1.withdrawl()
a1.get_bal()