'''
Kisi bhi object oriented programming, main hamesha constructor hoga

Constructor ek object bananeke liye madad karta hein

kabhi kabhi hamlog arguments pass karkey object banana chahtey hein, to aisey mein constructors hamey initialization karney mein madad kartey hein

__init__ - Method

'''

# hamney jo tarika dekha tha class Person ka vo apni jagah theek hein par ye wala bhi dekhtey hein


# class Person:
#     name = "Sadiq"
#     occ = "Developer"
    
#     def info(self): # koi bhi method aap likhogey to usko self parameter chahiye inside a class
#         print(f"{self.name} is  a {self.occ}")


class Person:
    def __init__(self):     # ye ek special method hein jo hamey constructor bananey ke liye madad karta hein
        self.name = name
    
    def info(self): # koi bhi method aap likhogey to usko self parameter chahiye inside a class
        print(f"{self.name} is  a {self.occ}")
        
        

a = Person()
# print(a.name)

'''
main idhar 'a.name' aur 'a.occ' mein 'divya' dena chahtha hun to main ye kaisey karunga to ye values main ismey dynamically store karna chahta hun 

'''

a.name = "Divya"
a.occ = "HR"
a.info()