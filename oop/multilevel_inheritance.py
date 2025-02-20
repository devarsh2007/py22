class person1:
    def read(self):
        print("i can read....")
        
        
class person2(person1):
    def write(self):
        print("i can write....")
        
class person3(person2):
    def speak(self):
        print("i can speak...")
        
p1 = person1()
p2 = person2()
p3 = person3()

p1.read()

p2.read()
p2.write()

p3.read()
p3.write()
p3.speak()