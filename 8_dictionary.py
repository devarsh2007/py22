student = {"name":"devarsh","age":17,"gender":True,"mobile":1234567890}
d1 = dict(age="a",name="b")
# print(student[0])  dictionery does not support indexing

print(student["name"])
print(student["mobile"])
print(student)
print(type(student))

student["age"] = 45
print(student)

#dict methods
d1 = {"a":1,"b":2,"c":3}
d2 = d1.copy()  #copy dict
print(d2)

values = d1.items()   # items return key and values in tuple all tuples in list
#convert to list and tuple
print(list(values))   
print(tuple(values))

print(list(d1.keys())) #give only keys of dict in list 
print(tuple(d1.keys()))

print(list(d1.values())) #give only values from dict in list
print(tuple(d1.values()))

d1.pop("b") #remove given keys and its value
print(d1)

d1["d"] = 4   # add new element in dictionary
print(d1)

d1.popitem()  # remove only last key and value pair
d1.popitem()
print(d1)

d1.update({"f":5,"g":6,"i":8})  #add new dictionary to d1
print(d1)