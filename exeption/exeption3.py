try:
    a = int(input("enter 1 for read file : "))   #value error
    if a==1:
        file = open("new.txt")          #filenotfound error
        print(file.read())
        file.close()
    
    
except(FileNotFoundError,ValueError):
    # print("error : ",e)
    print("file is not found!!!")
    
    
finally:
    print("good bye....")
    
# handle multiple error 

# finally runs if try block raise exeption or not
