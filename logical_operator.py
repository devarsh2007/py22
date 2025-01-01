a = input("eneter number1 : ")
b = input("eneter number2 : ")
c = input("eneter number3 : ")

print(a==b and a==c)
print(a==b or a==c)

print(not(a>b))

print(not(a==b and a>b))
print(not((a==b and a>b) or (c>a and c==a)))
            #   not(false  or   False)
            # True
            
print(not(not(a==b or a>b) or not(c==b and c!=b)))
                # False or true
                # not(true) = false