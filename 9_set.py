# numbers = {1,4,3,5,2}

# print(type(numbers))

color = {'red','red','blue','green','black'}
print(color)

# set methods
color.add('yellow')  #add element to set
print(color)

color.add('red')
print(color)

color.remove('green')   #remove element to set
print(color)

color.clear()
print(color)

# set operation
# 1) union - return all unique value between 2 set
s1 = {1,2,3,5,6}
s2 = {4,5,6,3,2}

print(s1.union(s2))
print(s2.union(s1))

# 2) intersection - return all comman value between 2 sets
print(s1.intersection(s2))
print(s2.intersection(s1))

# 3) difference - return all different value from first set to 2 set
print(s1.difference(s2))
print(s2.difference(s1))
