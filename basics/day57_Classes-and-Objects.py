'''
'class' - banta hein class keyword ke madad se  

'self' - parameter is the reference to the current instance of the class
       - self ka kya matlab hein, vo object jiskey liye method call ho raha hein

'''

class Person:
    name = "Harry"
    occupation = "Software Developer"
    networth = 10
    
    def info(self):     # agar class ke andar function likhrahey ho to hamesha self likhna heen hein
        print(f"{self.name} is a {self.occupation}")
    
a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "Accountant"

print(a.name, a.occupation)


a.info()   # idhar jab main 'a' wali object call kar raha hun to ye wo object hogi jispar self call kar rahi hogi 

b.info()   # aur jab idhar 'b' wali object call karegi to ye wo object h

c.info()   # idhar mainey kuch bhi initialize nahi kara hein to default values heen lengey

