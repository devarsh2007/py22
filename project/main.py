from datetime import date
import seller as s
import customer as c
import mysql.connector as con
db = con.connect(user="root",password="",database="py22",host="localhost")

mycursor = db.cursor()


choise = int(input("1 for customer view , 2 for seller view : "))
if choise==1:
    name = input("enter your name : ")
    address = (input("enter your address : "))
    mobile= (input("enter your mobile : "))
    c.adduser(name,address,mobile)
    
    uid = c.uid(name)
    
    print("\n----------- select your product ------------")
    products = s.view()

    head = ["id","name","price","details"]
    print(head)
    
    for i in products:
        print(i)
    print("--------------------------------------------")
    choise = int(input("enter product id to buy : "))
    for i in products:
        if i[0]==choise:
            payment = int(input("1 for payment & 0 for cancel :"))
            if payment==1:
                print("payment success....")
                # -----------------------
                sql = "select price from products where id = %s"
                values=(choise,)
                mycursor.execute(sql,values)
                data = mycursor.fetchone()
                amt = int(data[0])
                # print(amt)
                # -----------------------  
                
                # -----------------------
                today = date.today()
                sql = "insert into payments values(%s,%s,%s,%s,%s)"
                values=["",uid,choise,amt,today]
                mycursor.execute(sql,values)
                # print("payment added successfuly...")
                # -----------------------
                
            else:
                print("canceled payment....")
         
        
               
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
        print(s.view())
        
    else:
        print("invalid input.....")
    
else:
    print("invalid input!!")
    
db.commit()