# write a program that take string and make a dictionary key id latter and value is count
# check frequncy of string
# hello {h:1 , e:1 ,l:2 ,l:2 ,o:1 }

name = input("enter string : ")
d1 = {}
for i in name:
    cnt = name.count(i)
    d1[i] = cnt

print(d1)

