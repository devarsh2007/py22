# single level inheritance
class person: #perent
    name = "python"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def walk(self):
        print("i can walk....")
        
    def talk(self):
        print("i can talk...")
        

class student(person):  #child
    def __init__(self, name, age,roll):
        super().__init__(name, age)
        self.roll = roll
    
    def read(self):
        print("i can read...")

    def details(self):
        print(self.name)
        print(self.age)
        print(self.roll)
        
# p1 = person("devarsh",17)
# p1.walk()
# p1.talk()

s1 = student("devarsh",17,121   )
s1.read()
s1.walk()
s1.talk()
print(person.name)
s1.details()