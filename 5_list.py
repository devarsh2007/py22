# []
student = ["devarsh patel",17,98.99,True]
print(student)

number = [1,2,3,4,5,6,7]
print(type(number))

print(student[0])
print(len(number))
print(student[len(student)-1])

print(student[-1])
print(student[-2])

# list_name[start : stop : size]
# list_name[0 : stop : 1]

print(number[0:3])
# 1357
print(number[0::2])
# 764321
print(number[-1::-1])
# 7,3
print(number[-1::-4])

print(student+number) #concatination - merge
print(number*3)     #repeatetion
print(student*2)