class Test:
    def __init__(self):          #constructor
        print("test class-CM")

    def m1(self):                 #is instance
        print("test class-IM")

    @classmethod
    def m2(cls):
        print("test class-class method")

    @staticmethod
    def m3():
        print("test class- static method")


t1=Test()
t1=Test()

t1.m1()
t1.m2()
t1.m3()