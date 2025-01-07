# write a program that perform opration like calc

print("-----------operation-----------")
print("1 for addition\n2 for subtraction\n3 for multiplication\n4 for division\n5 for power")

choise = int(input("enter your choise : "))

if choise>0 and choise<6:
    # print("ok")
    a=float(input("enter number1 : "))
    b=float(input("enter number2 : "))
    
    if choise==1:
        print(f"addition of {a} and {b} is {a+b}")
        
    elif choise==2:
        print(f"subtraction of {a} and {b} is {a-b}")
        
    elif choise==3:
        print(f"multiplication of {a} and {b} is {a*b}")
        
    elif choise==4:
        print(f"division of {a} and {b} is {a/b}")
        
    elif choise==5:
        print(f"base {a} and power {b} is : {a**b} ")
    
else:
    print("invalid choise!!!")