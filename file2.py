# file_obj = open("LESSON.txt",'a')

# print("new file created....")

print("1 for create a new file\n2 for read existing file")
choise = int(input("enter your choise : "))

if choise==1:
    filename = input("enter file name : ")
    file = open(filename,'w')
    print(f"{filename} is created....")
    
elif choise==2:
    filename = input("enter file name : ")
    file = open(filename,'r')
    print(f'---------------- {filename} -------------------')
    print(file.read())
    
