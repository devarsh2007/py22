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