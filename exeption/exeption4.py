l1=["a","b","c"]
try:
    a = int(input("enter a number : "))  #valueerror
    for i in range(0,a):     #out of range error
        print(l1[i])
    
except ValueError:
    # print(v)
    print("give int number....")
    
except IndexError:
    print("give proper index....")
    
finally:
    print("good bye....")
