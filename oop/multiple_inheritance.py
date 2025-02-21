class student:
    def __init__(self,balance):
        self.__balance = balance
    
    def read(self):
        print("i can read....")
        
    def abalance(self):
        print(self.__balance)
        
class employee:
    def work(self):
        print("i can work....")
        
class person(student,employee):
    def __init__(self, balance):
        super().__init__(balance)
        
    def details(self):
        print("i am person...")
        
p1 = person(1000)
p1.read()
p1.work()
p1.details()

# print(p1.__balance)  not valid
s1 = student(2000)
# print(s1.__balance)

# accessing private variable
s1.abalance()
print(s1._student__balance)