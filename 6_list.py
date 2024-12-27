l1 = ["red","green","red","yellow","blue","black"]
# l2 = list(1,2,3,4)
print(l1)
l1[4] = "white"
print(l1)
n1=[0,1,2]
# print(l1[(len(l1)-1)][2])
# print(l1[(len(l1)-1)][0])

# list methods
l1.append(3)  #add element at last position
print(l1)


l1.extend(n1)  #merge 2 list
print(l1)

l1.insert(0 , "grey")    #add element at give position of list
l1.insert(3 , "orange")
print(l1)

l1.remove("orange")  #remove given element
l1.remove(2)
print(l1)

l1.pop(0)   #remove element from given position
l1.pop(len(l1)-1)
print(l1)

print(l1.index("red"))  #return index of element
print(l1.index(0))

print(l1.count("red"))   # count items appears in list
print(l1.count(0))

numbers = [10,4,8,2,30]
print(numbers)
numbers.sort()    #sort the list in accending order
print(numbers)
numbers.sort(reverse=True)  # sort list in desending order
print(numbers)

numbers = [5,4,7,92]
numbers.reverse()    #reverse the order of item
print(numbers)

n2 = numbers.copy()   #copy the list into another list
print(n2)

numbers.clear()    #clear all items from list
print(numbers)