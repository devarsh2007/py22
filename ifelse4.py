# write a program that check a number is palimbrome number or not
# 121 => reverse =>121
# 323 => 323 => this is palimbrome number

number = int(input("enter number : "))

number = str(number)

# print(number[-1::-1])
reverse = number[-1::-1]
if reverse == number:
    print(f"{number} is palimbrome number")
    
else:
    print(f"{number} is not palimbrome number")