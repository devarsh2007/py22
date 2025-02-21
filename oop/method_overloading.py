# method overloading

class calc:
    def multiply(self,a=None,b=None):
        if a==None and b==None:
            return 0 
        
        elif a!=None and b==None:
            return a*a
         
        else:
            return a*b
        
c1 = calc()
print(c1.multiply())
print(c1.multiply(5))
print(c1.multiply(5,10))