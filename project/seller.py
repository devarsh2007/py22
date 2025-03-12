# connection to mysql
import mysql.connector as con
db = con.connect(user="root",password="",database="py22",host="localhost")

mycursor = db.cursor()

def add():
    sql = "insert into products values(%s,%s,%s,%s)"

    name = input("enter product name : ")
    price = int(input("enter product price : "))
    details= input("enter product details : ")

    values=["",name,price,details]

    mycursor.execute(sql,values)
    print("product added successfuly...")

def remove():
    sql = "delete from products where id=%s"

    id = int(input("enter product id to delete : "))

    values=[id]

    mycursor.execute(sql,values)
    print("product deleted successfuly...")

def edit():
    sql = "update products set name=%s,price=%s,details=%s where id=%s"

    id=int(input("enter product id : "))
    name = input("enter new product name : ")
    price = int(input("enter new product price : "))
    details= input("enter new product details : ")

    values=[name,price,details,id]

    mycursor.execute(sql,values)
    print("product updated successfuly...")

def view():
    sql = "select * from products"
    mycursor.execute(sql)
    data = mycursor.fetchall()
    # print(data)
    return data
    
    # searching algorithm
    # name = input("enter name : ")
    # for i in data:
    #     if i[1] == name:
    #         print(i)
  
db.commit()
  