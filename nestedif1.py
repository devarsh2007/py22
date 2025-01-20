# write program that check maximum number between 3 numbers
a=int(input("enter number1 : "))
b=int(input("enter number2 : "))
c=int(input("enter number3 : "))

# 5 2 1
# 2 4 1
# 4 5 10
# 5 4 10
if a>b:
    if a>c:
        print("a is max")
        
    else:
        if a==c:
            print("a and c are max")
            
        else:
            print("c is max")
    
else:
    if b>c:
        print("b is max")
    
    else:
        if c==b and c==a:
            print("all are same")
        else:
            print("c is max")
        
    
