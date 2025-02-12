

try:
    a = str(input("enter number : "))
    print(a)
    
    # error
    a = ["a","b","c","d","e"]
    for i in range(0,6):
        print(a[i])
except:
    print("error ocured....")
    
print("last line of code....")
