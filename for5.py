string = "abcdefghijklmnopqrstuvwxyz"
l1 = [1,2,3]
t1 = (8,9,0)
s1 = {6,5,4}
d1 = {"a":1,"b":2,"c":3}

for i in string:
    print(i,end=" ")
print("")

print("-"*100)
for i in l1:
    print(i)

print("-"*100)
for i in t1:
    print(i)

print("-"*100)
for i in s1:
    print(i)
    
print("-"*100)
for i in d1.items():
    print(i)
