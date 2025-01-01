l1 = [1,2,3,4,5,6,7,8,9,10]
print(10 in l1)

n=100
print(n in l1)

print(n not in l1)
print(4 not in l1)

n = int(input("enter element to find : "))
print(f"list status : {n in l1} at index {l1.index(n)}")

# ----------------------------------------------------------
# find element present in dict value
print("\n")
d1={"a":1,"b":2,"c":3,"d":4}

n = (input("enter key to find : "))
print(f"dictionary status : {n in d1}")

n = int(input("enter value to find : "))
print(f"dictionary status : {n in d1.values()}")