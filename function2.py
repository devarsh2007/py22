# with argument without retun value function
def add(a,b):
    print("addition : ",a+b)
    
a1 = int(input("enter number 1 : "))
b1 = int(input("enter number 2 : "))
add(10,30)
add(0,-2)

add(a1,b1)

# without argument with return value function
def getpi():
    return 3.14159265359

print(getpi())

# with argument with return value function
def area(r):
    print(f"circle area : ",getpi() * (r**2))
    return getpi() * (r**2) 

ans = area(10)
print(round(ans,2))

# with argument without return value funtion
print("hello world")
# print(e)