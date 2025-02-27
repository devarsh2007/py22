a =10   #global variable
b=5

def add():
    global a,b  
    a = 20  #local variable
    print(a)
    b+=5
    

add()
print(a)

print(b)

# dir
import modules.mypackage.mymaths as mymaths
import module1

# print(dir(mymaths))
l1 = dir(mymaths)
# print(l1[0])

print(dir(module1))