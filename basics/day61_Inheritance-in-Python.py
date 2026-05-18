'''
---> Inheritence in Python <---
Kaisey Main ek existing class ko extend karkey ek totally nayi class banasakta hun

'''

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id 

    def showDetails(self):
        print(f"The name of Employee : {self.id} is {self.name}")

# Employee ke aisey ham kai saarey objects bana saktey hein 
e = Employee("Rohan Das", 400)
e.showDetails()

# Assuming ki ye Employee Class Bani Padi hein, aur currently use bhi kai saarey log kar rahey hein to agar main suddenly is class ko change kardun to code base main to aafat ajayegi, isiliye main best isko inherit karlunga 

class Programmer(Employee):    
    def showLanguage(self): # kya main EMployee par showLanguage chala sakta hun, nahi
            print("The default Language is Python")

# Ye Obviously nahi chalega, kyunki ye function Employee par defined nahi hein
# e.showLanguage()

e2 = Programmer("Harry",4100)
e2.showDetails()

# kai tarah ke inheritence hoti hein, vo ham next class mein dekhengey