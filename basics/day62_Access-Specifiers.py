'''
Python Programming mein jab aap inhertence kartey hein to access specifiers kis tarah se kaam kartey hein , aur kya exact rule se ye sab kaam kartey hein vo dekhtey hein chaliye

Python main public, private ,protected aisey koi cheex nahi hoti , ye pehli baat , phir bhi ham log iskey baarey mein baat kartey hein kyun ?

dono pehlun samjtey hein ki, kya hein access modifiers honey ya na honey ki kya pehlu hein dekhtey hein chaliye
'''


'''
In-General --> OOPS in any Language 

Jab Bhi ham class banatey hein unkey variables by default public hotey hein 

PUBLIC - Class ke bahar sey bhi access kiya ja saktey hein 

PRIVATE - Bahar se access nahi kiya ja sakta

PROTECTED - ye jo hein vo class ke andar se access kiya ja sakta hein, aur sub class se access kiya ja sakta hein

'''

# Ab Python main aatey hein ki ye Python main hotey bhi kyun hein aur kyun nahi hotey


class Employee:
    def __init__(self):
        self.name = "Harry"

# Here name is a publicly accessble variable 
a = Employee()
print(a.name)

# private ka matlab hein access nahi kiya ja sakta 

'''
Agar kisi bhi variable to double underscore se prefix kardo to main usey access nahi karpaunga

Python main aisa koi strict concept nahi hein , jaisey ki java main hein 

Python main sirf ek convention ke liye kisibhi variable ke aagey double underscore laganey se , ek weak internal indicator hoga ki ye particular variable private hein , jo ki still accessible hein

Access Karney ke liye class ka name with a underscore 
'''

class EmployeePriv:
    def __init__(self):
        self.__namepriv = "Sadiq is private varible"

a1 = EmployeePriv() 
print(a1._EmployeePriv__namepriv) # Cannot be accessed directly but can be accessed  indirectly

# print(a1.__dir__()) to is waley output main dekhogey to __namepriv nahi milega tumhein

# To ye Indirectly kyun access ho pa raha hein because of 'Name Mangling' in Python


'''
Python jahan bhi double underscore laga hoga vahan mangling kardega bas aur directly access nahi karsaktey
Name Mangling jo hein , vo aisa hein usmey private attibute/varibale jo hein uska naam badal ke rak diya jaata hein

Agar main ye --> print(a1.__dir__()) chalun to a1 ke saarey possible methods pata chalti hein
to ye name mangling ka concept isilye aaya taki koi accidently varibales ko override na karey , isiliye a single underscore followed by a double underscore lagaya jaata hein taaki convention maintain ho
'''
# Important - Python apney aap se Private, Protected aur Public kuch nahi enforce karta ye just ek convention hein jo ki follow hota hein


'''
Protected - Accessed within the class and the Subclass 

Varible prefixed with a single underscore is considered protected 

yahan protected mein kyunki sirf single underscore laga rahey hein to mangling nahi hogi
'''

class Student:
    def __init__(self):
        self._name = "Sadiq"

    def _funName(self):      # protected method
        return "Sadiq"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj)) # idhar mujhey _name miljayega to yahan par mangling nahi ho raha hein , to aap log isey directly access karsaktey ho , par ye as a convention use kiya jaata hein

print("-----After Protected-----")
# calling by object of Student class
print(obj._name)      
print(obj._funName())     
# calling by object of Subject class
print(obj1._name)    
print(obj1._funName()) 
