import json

emp_json="""{
    "eid":"101",
    "ename":"Rahul",
    "esal":"none",
    "avail":"true",
    "loc":"undefined"
}"""

print(emp_json)
emp_dict=json.loads(emp_json)
print(type(emp_json))
print(type(emp_dict))
print(emp_dict)


