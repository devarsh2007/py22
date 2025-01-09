# grade calculator
maths = int(input("enter maths marks : "))
eng = int(input("enter english marks : "))
science = int(input("enter science marks : "))

if (maths>=0 and maths<=100) and (eng>=0 and eng<=100) and (science>=0 and science<=100) : 
    # print("ok")
    total = (maths + eng +science) / 3
    total = round(total,2)
    print(f"percentage : {total} %")
    
    if total>=90 and total<=100:
        print("Grad : A+")
        
    elif total>=80 and total<=89:
        print("Grad : A")
        
    elif total>=70 and total<=79:
        print("Grad : B")
        
    elif total>=60 and total<=69:
        print("Grad : C")
        
    elif total>=50 and total<=59:
        print("Grad : D")
        
    elif total>=40 and total<=49:
        print("Grad : E")
        
    else:
        print("you are fail.....")
    
else:
    print("enter valid marks !!!")