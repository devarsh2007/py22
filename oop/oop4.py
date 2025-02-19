class bank:
    # class variable
    bankname = "state bank of india"
    
    def __init__(self,name,ifsc,balance):
        #instance variable
        self.name = name
        self.ifsccode = ifsc
        self.balance = balance
        
    def deposite(self,amount):
        self.balance = self.balance + amount
        print("your current balance is : ",self.balance)
        
    def withdraw(self,amount):
        if self.balance < amount:
            print("invalid amount for withdraw")
            
        else:
            self.balance-=amount
        
        print("your current balance is : ",self.balance)
                    
        
    def details(self):
        print("account holder name : ",self.name)
        print("ifsc code : ",self.ifsccode)
        print("total balance : ",self.balance)
        
# a1 = bank("devarsh","sbin001",20000)
# a1.details()
# print(a1.bankname)   #class variable with obj
# print(bank.bankname)   #class variable with class name

print("your bank : ",bank.bankname)
a2 = bank("druv","sbi002",5000)
a2.details()
a2.deposite(2000)
a2.withdraw(3000000)  # not success
a2.withdraw(3000)    # success

a2.details()