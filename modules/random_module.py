from random import *
# import random as r

# 0.0 - 1.0
print(random())

#give range - float
print(uniform(1,10))

#give range - int
print(randint(1,100))

# give range with gaps - int
print(randrange(0,100,10))

# return element from list
l1=["a","b","c","d"]
print(choice(l1))

# return multiple ele from list
print(choices(l1,k=2))

# shuffle a list elements
print(l1)
shuffle(l1)
print(l1)

l1 = [1,2,3,4,5]
print(sample(l1,3))
# s = [1,2,3,4,5]
# s=[2,3]
print(l1)
