# import
# 1) import module_name  
# 2) from module_name import fun,var...

import mymaths as m

a= int(input("enter number1 : "))
b= int(input("enter number2 : "))

m.add(a,b)
m.sub(a,b)
m.mul(a,b)
m.div(a,b)

print(m.pi)

print("good bye...")