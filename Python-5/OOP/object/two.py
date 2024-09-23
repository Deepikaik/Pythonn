class Employee:       #class
    loc="B101"

e1=Employee()       #objects
e2=Employee()
e3=Employee()

print(id(e1))        #printing objects id is a function
print(id(e2))
print(id(e3))
print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)
print(Employee.__dict__)
