try:
    a=int(input("enter a number"))
    b=int(input("enter another number"))
    print(a/b)

except ZeroDivisionError as e:
    print("cant be divisible by zero")

except ValueError as e:
    print("cant convert str to int")