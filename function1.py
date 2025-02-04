# user define
# function define
def printline():
    print("---------------------------------------------")
    
# printline() function call
# printline()
# printline()
# print("function") 
# printline()
# printline()
# printline()

# 1-10
# 1 x 1 =1

# without argument without return value function
def table():
    start = int(input("enter starting number : "))
    end = int(input("enter ending number : "))
    # count=1
    for j in range(start,end+1):
        for i in range(1,11):
            print(f"{j} x {i} = {j*i}")
            
        printline()
        # count+=1
        
table()