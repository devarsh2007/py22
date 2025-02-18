class person:
    # cunstructor
    def __init__(self):
        print("cunstructor called...")
        
    def walk(self):
        print("this is walk method...")
        
    def talk(self):
        print("this is talk method...")
        
obj = person()
obj.walk()
obj.talk()