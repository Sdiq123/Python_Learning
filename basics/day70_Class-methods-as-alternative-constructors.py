'''
------> Using Class Methods as Alternative Constructors <-------------
kabhi kabhi hamrey paas data ek certain format mein hota hein , aur aisey mein agar ham constructor ko data galat tarikey/format se paas karengey to definitely error throw karega
-> to obviously hamey data ko pehley parse karna padta hein , phir constructor ko data pass karna padta hein, class methods ko as a alternative constructor use karkey ham is problem ko solve karsaktey hein 
'''
# Neechey wala commented code bhi ek baar padlo

'''
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

e1 = Employee("Sadiq", 12000)
print(e1.name)
print(e1.salary)


string = "Harry-12000"  # ab hamey koi aisa input de raha hein string ke format mein, to ye hamey parse karkey lena padega
e2 = Employee(string.split("-")[0],string.split("-")[1] )
print(e2.name)
print(e2.salary)

# To aisey karkey to main seekhlunga par phir bhi kya mera code ugly nahi dikhega iske baad sey , par ye sirf '-' isko handle hua hein, agar dusrey format mein ayega to kya ye handle hoga? ue hamey sochna hein
'''

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0],int(string.split("-")[1]))

e1 = Employee("Sadiq", 12000)
print(e1.name)
print(e1.salary)


string = "Harry-12000"  # ab hamey koi aisa input de raha hein string ke format mein, to ye hamey parse karkey lena padega
e2 = Employee.fromStr(string)   # to yahan pe ye instance bangaya with these parameters , ya karkey jo bhi messed up wala code tha vo hamney utha kar class ke andar daal diya, mess aapkey class ke andar hoga main code main nahi hoga
                                # Constructr sirf initialize karkey chodta hein, ye ek particular format ke data ko
print(e2.name)
print(e2.salary)