class Employee:
    company_name='TCS'                 #static variable
    def __init__(self,id,name,sal):    #self is an instance variable
        self.eid=id
        self.ename=name
        self.esal=sal


e1=Employee(101,'Rahul',45000)
e2=Employee(102,'Sonia',55000)
e3=Employee(103,'Priya',65000)

print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)