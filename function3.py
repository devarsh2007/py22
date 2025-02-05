# multiply 2 numbers
# default argument
def multiply(a=1,b=1):
    print("multiplication : ",a*b)
    
multiply(2,3)
multiply(5)
multiply()

print("-------------------------------------------------------")

# keyword argument
def subjects(eng,maths,science):
    print("english : ",eng)
    print("maths : ",maths)
    print("science : ",science)

# subjects(10,20,50)
# subjects(50,20,10)
# print("="*100)
# subjects(10,30,40)
subjects(science=50,maths=20,eng=10)

print("--------------------------------------------------------")

# return multiple values
def calc(a,b):
    add = a+b
    sub = a-b
    multi = a*b
    div = a/b
    return add , sub , multi , div

t1 = calc(10,20)
print("addition : ",t1[0])
print("subtraction : ",t1[1])
print("multiplication : ",t1[2])
print("division : ",t1[3])

print("----------------------------------------------------------")

# arbitary argument
def add(*n):
    sum=0
    # print(n)
    # sum = n[0]+n[1]+n[2]
    # print(sum)
    for i in n:
        sum+=i
        
    return sum
    
print(add(1,2,3))
print(add(10,20,30,40,50,60,70,80,90,100))
print(add(1,1,1,1,1))
