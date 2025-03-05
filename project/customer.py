import mysql.connector as con
db = con.connect(user="root",password="",database="py22",host="localhost")

mycursor = db.cursor()

def adduser():
    sql = "insert into users values(%s,%s,%s,%s)"

    name = input("enter your name : ")
    address = (input("enter your address : "))
    mobile= int(input("enter your mobile : "))
    
    values=["",name,address,mobile]

    mycursor.execute(sql,values)
    print("user added successfuly...")
    

def addpayment():
    sql = "insert into payments values(%s,%s,%s,%s,%s)"
    
    uid = 0
    pid = 0
    amount= 0
    date = 0

    values=[]

    mycursor.execute(sql,values)
    print("payment added successfuly...")



db.commit()