a = float(input("enter number 1 : "))
b = float(input("enter number 2 : "))

print(a+b)
print(a-b)
print(a*b)
print(a/b)

# modulas
print(a%b)

#exponent
print(a**b)

#floor division
print(int(a//b))
print("\n")
# --------------------------------------------
# 2,4 -> 4,2  -> swaping
a = int(input("enter num1 : "))
b = int(input("enter num2 : "))

print("before swap : ")
print(f"a : {a}")
print(f"b : {b}")

c=a
a=b
b=c
print("after swap : ")
print(f"a : {a}")
print(f"b : {b}")