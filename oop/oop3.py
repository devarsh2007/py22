class student:
    def __init__(self,name,age,roll):
        print("cunstructor called...")
        #instance variables
        self.name = name   
        self.age = age
        self.roll = roll
        
    def details(self):
        print("name : ",self.name)
        print("age : ",self.age)
        print("roll no : ",self.roll)
        
s1 = student("devarsh",17,101)
s1.details()

s2 = student("dhruv",23,201)
s2.details()
