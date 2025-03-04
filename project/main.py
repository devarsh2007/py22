import seller as s

choise = int(input("1 for customer view , 2 for seller view : "))
if choise==1:
    name = input("enter your name : ")
    address = input("enter your address : ")
    mobile = input("enter your mobile : ")
    
    
    
    
elif choise==2:
    print("1-add\n2-remove\n3-edit\n4-view")
    choise = int(input("enter your choise : "))
    
    if choise==1:
        s.add()
        
    elif choise==2:
        s.remove()
    
    elif choise==3:
        s.edit()
        
    elif choise==4:
        s.view()
        
    else:
        print("invalid input.....")
    
else:
    print("invalid input!!")