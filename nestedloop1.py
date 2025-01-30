# # print following pattern
# *
# **
# ***
# ****

n = int(input("enter number : "))
symbol= input("enter a symbol : ")

# count = 1
for j in range(n):
    for i in range(j+1):
        print(symbol,end=" ")
    print("")
    # count += 1

# for i in range(2):
#     print("*",end=" ")
# print("")

# for i in range(3):
#     print("*",end=" ")
# print("")

# for i in range(4):
#     print("*",end=" ")
# print("")
