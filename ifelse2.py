# check number is even or odd
# even => 2,4,6,8
# odd => 1,3,5,7,9...

number = int(input("enter a number : "))
if number%2 == 0 :
    print(f"{number} is even")
    
else:
    print(f"{number} is odd")