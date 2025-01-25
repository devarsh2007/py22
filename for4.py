# write a program that find a string or number is palimbrom or not
# 101 
# madam

text = input("enter a string : ")

# reverse a string
# print(text[-1::-1])
reverse = text[-1::-1]

if text==reverse:
    print(f"{text} is palimbrom")
else:
    print(f"{text} is not palimbrom")

# last = len(text)-1
# for i in range(len(text)):
#     print(text[last],end="")
#     last-=1

# print(text[last])
# last-=1
# print(text[last])
# last-=1
# print(text[last])
# last-=1
# print(text[last])