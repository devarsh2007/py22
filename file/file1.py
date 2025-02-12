# open
# operation
# close

exe_file = open("exercise.txt")
print(exe_file)
# first way to read file
for i in exe_file:
    print(i)
    
exe_file.close()

f1 = open("demo.txt")
# for i in f1:
#     print(i)
#     print("-----------------------------------")
# f1.close()

# second way to read a file
file = open("demo.txt",'r')
# read no of charecters
print(file.read(1)) 

# read all charecters
print(file.read())
file.close()
