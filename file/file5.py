import os
os.rename("basics.txt","symbol.txt")

os.remove("text.txt")

# create new folder 
os.mkdir('directory')

# change current directory
os.chdir('./directory')
# file = open('demo.txt','r')
# print(file.read())
# file.close()

# print current working directory
print(os.getcwd())

os.chdir('../')
print(os.getcwd())

# remove directory
os.rmdir('directory')
os.rmdir('text')