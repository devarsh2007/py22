
# creating class
class person:
    def walk(self):
        print("this is walk method...")
        
    def talk(self):
        print("this is talk method...")
        
    def add(self,a,b):
        print(a+b)
        
# creating object
p1 = person()
p1.walk()   #calling walk method
p1.talk()   #calling talk method

# creating another object
p2 =  person()
p2.walk()

p3 =person()
p3.add(2,3)