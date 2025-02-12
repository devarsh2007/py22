obj = open("text.txt","w")
obj.write("my name is devarsh....")
obj.write("\nhello world")
obj.close()

print("data writen in file....")

obj2 = open("text.txt","a")
obj2.write("\nthis is new line....")
obj2.write("\ndef add(a,b):\n     print('addition : ',a+b)")
obj2.close()

obj2 = open("text.txt","r")
print(obj2.read())
obj2.close()