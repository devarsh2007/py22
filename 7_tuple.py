employee = ("devarsh",10000000,17,50.7,True,17,17)
t1 = tuple(1,2,3,4,5)
print(employee)
print(employee[0])
print(employee[1:4])
print(employee[-1::-1])

# employee[0] = "param"   it is not changable  - immutable

# tuple method
print(employee.count(17))
print(employee.count("devarsh"))

print(employee.index(17))