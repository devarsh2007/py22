name = "the easy learn"
print(name.upper())
print(name.lower())

print(name.isalnum())
print(name.isdigit())
print(name.islower())

l1 = ["a","b","c"]
text = " "
print(text.join(l1))

text = "1 2 3 4 1"
print(text.replace("1","10",1))
print(text)

text ="hello world"
l1 = text.split()
print(l1)

import mypackage.mymaths as m
m.add(1,2)