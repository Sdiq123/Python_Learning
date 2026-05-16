'''
Kisi bhi object oriented programming, main hamesha constructor hoga

Constructor ek object bananeke liye madad karta hein

kabhi kabhi hamlog arguments pass karkey object banana chahtey hein, to aisey mein constructors hamey initialization karney mein madad kartey hein

__init__ - Method , hamesha invoke hoga jab bhi ham ek naya object banayengey vo class ka

'''

# hamney jo tarika dekha tha class Person ka vo apni jagah theek hein par ye wala bhi dekhtey hein


# class Person:
#     name = "Sadiq"
#     occ = "Developer"
    
#     def info(self): # koi bhi method aap likhogey to usko self parameter chahiye inside a class
#         print(f"{self.name} is  a {self.occ}")


class Person:
    def __init__(self,name,occ):     # ye ek special method hein jo hamey constructor bananey ke liye madad karta hein
        print("Hey I am a person")
        self.name = name
        self.occ = occ
    
    def info(self): # koi bhi method aap likhogey to usko self parameter chahiye inside a class
        print(f"{self.name} is  a {self.occ}")
        
        

a = Person("Harry", "Developer" )  # jab bhi main object banaunga to directly constructor ko call karunga  
# jab bhi main a = Person() call karun to vo directly print karega, mujhey separately call karney ki zarurat nahi hein
b = Person("Divya", "HR")   # idhar self as a object parameter pass ho raha hein,matlab 'self' ki jagah b pass ho rahah hein , to teen arguments pass karney ki zarurat nahi hein
# ab jab main dusra object banaunga to bhi default __init__ method directly call hoga 
c = Person()

a.info()
b.info()
# print(a.name)

'''
main idhar 'a.name' aur 'a.occ' mein 'divya' dena chahtha hun to main ye kaisey karunga to ye values main ismey dynamically store karna chahta hun 

'''

# a.name = "Divya"
# a.occ = "HR"
# a.info()

'''
Constructor ka main kaam hein value ko initialize karna aur vo hamesha None return karega
Two types of Constructors 
1. Parameterized Constructor 
2. Default Constructor - jo arguments nahi leta aur sirf self leta hein

'''