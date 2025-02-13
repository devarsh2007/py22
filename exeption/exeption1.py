

try:
    a = int(input("enter number : "))
    print(a)
    
    # error
    a = ["a","b","c","d","e"]
    for i in range(0,6):
        print(a[i])
        
except Exception as e:
    print("error ocured....")
    print("error : ",e)
    
    
print("last line of code....")
