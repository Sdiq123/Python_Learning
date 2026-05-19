'''
----------> super Keyword <---------
kabhi kabhi ham logon ko child class se parent class ke methods ko call karney ki zarurat padti hein aur aisa karney ke liye ham super() - keyword ka istemaal kartey hein

super keyword is used to refer the parent class 
'''

# uncomment and check it out
'''
class ParentClass:
    def parent_method(self):
        print("This is the parent method.")

class ChildClass(ParentClass):
    def child_method(self):
        print("This is the child method.")
        super().parent_method() # Agar mujhey ek parent method ko call karna hein apney child class mein after inheritence , to main usey ' super ' - keyword ke madad se heen call karunga

child_object = ChildClass()
child_object.child_method()
'''

# There is something called as 'dry' principal - hamey apney aap ko kabhi bhi 'Repeat' nahi karna hein

class Employee:
    def __init__(self,name,id):
        self.name = name 
        self.id = id 
        
class Programmer(Employee):
    def __init__(self,name,id ,lang):
        # self.name = name 
        # self.id = id 
        super().__init__(name,id) # kyun repeaat karna hein , super ke init ko call karlo,aur usko uskey argumments de do 
        self.lang = lang
        
rohan = Employee("Rohan Das", "428")
Sadiq = Programmer("Sadiq Pasha", "284", "python")
print(Sadiq.name)