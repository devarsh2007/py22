# copy = input("enter file to copy : ")
# paste = input("enter file to paste : ")

# do = open(copy,"r")
# content = do.read()
# do.close()
# print("data copied....")

# to = open(paste,"a")
# to.write("\n\n")
# to.write(content)
# to.close()
# print("data pasted....")
v = 0
c = 0
n = 0
vowels=["a","e","i","o","u"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]
file = open("demo.txt","r")
for i in (file.read()):
    # print(i)
    if i in vowels:
        v+=1
        
    elif i in numbers:
        n+=1
        
    else:
        c+=1
    
    
print("vowels : ",v)
print("consonates : ",c)
print("numbers : ",n)
file.close()