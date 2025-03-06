import mysql.connector as con
db = con.connect(user="root",password="",database="py22",host="localhost")

mycursor = db.cursor()

def adduser(name,address,mobile):
    sql = "insert into users values(%s,%s,%s,%s)"
    values=["",name,address,mobile]

    mycursor.execute(sql,values)
    print("user added successfuly...")
    
def uid(name=0):
    sql = "select id from users where name = %s"
    
    values = [name]
    mycursor.execute(sql,values)
    data = mycursor.fetchone()
    return data[0]
    # print(data)

db.commit()