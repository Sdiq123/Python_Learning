'''
'dir()'  ,  '_dict_'  and  'help()'  Methods jo Python main Object Interospection karney ke liye istemaal hotey hein aur hamey kyun ye use karna hein jab ham nayi classes ke saath deal kartey hein 

'Object Interospection' - iska matlab hein ki hamko kisibhi Object main dekhna chahtey hein ki usmey kya-kya hein, aur kis tarah se usko use kiya ja sakta hein

Ek Class hamko di-gayi hein, anjaan class hein uskey baarey mein hamko kuch nahi pata, aur hamey use karney ke liye bol rahey hein, kaisey hamlog iskey baarey mein use karna seekh saktey hein 

'__dict__' ye ek attribute hein method nahi hein 

'''

# x = [1,2,3]
x = (1,2,3)
# Mujhey ek list Object ke baarey main jaanna hein ki kya kya methods hein 
print(dir(x)) # ye saarey available methods list ke related batata hein
print(x.__add__)

'''
dir() method ek data type ke saarey methods aur dunder methods ( jo double underscore ko prefix aur suffix kartey hein unko dunder methods boltey hein) jo return kartey hein 
-> usefull to dicover what you want to know about the object
'''

'''
__dict__   -   Method saarey cheezein dictionary mein deta hein

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.version = 1

p = Person("John", 30)
print(p.__dict__)  # self. -> karkey jo bhi mainey set kara hein vo saarey cheezein __dict__ -> method ke andar ajayengey as a dictionary


'''
help() - to ye saarey cheezein str ke baarey mein bolta hein , help to get the documentation , including the description of attributes and methods
'''

print(help(str))

print("-----After Person------")
print(help(Person))

