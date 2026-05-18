'''
Difference Between Instance Variables and Class Variables 
Instance Variable  -ham use kartey hein , jab hamey kisi bhi property ko associate karna padta hein ek particular object sey
Class Variable - use kartey hein jab hamey puri class ke liye variable banana padta hein jo ki saary instances share karnegey

'''

class Employee:
    companyName = "Apple"   # ye mera class variable hein, kyunki ye variable class se associated hein
    noOfEmployees = 0    # Obviously ye variable yahan ek class variable hein kyunki jo variable hein, vo har ek instance ke liye thodi na badega
    def __init__(self, name):   # yahan pe saarey variables instance se associated hein
        self.name = name 
        self.raise_amount = 0.02 # ye mera instance variable hein jo ki Instance se associated hein naki class se , kyunki har ek employee ka raise alag alag hoga rite
        Employee.noOfEmployees += 1 # jaisey jaisey employees add hotey jaye waisey wiasey ye number badta jaye 
    def showDetails(self):
        print(f"The name of the Emplyee {self.name} and the raise amount in {self.noOfEmployees} sized {self.companyName} is {self.raise_amount} ")

#Employee.showDetails(emp1)           # ye bhi ek heen cheez hein
emp1 = Employee("Harry")
# yahan par mujhey sirf Harry ko raisey dena hein  
emp1.raise_amount = 0.3 # main isko aisey change karsakta hun kyunki ye instance se associated hein 
emp1.companyName = "Apple India"    # kyunki ye emp1 se associated hein to pehley emp1 mein check karega aur sirf emp1 ko heen change karega , emp2 ko change nahi karega - kyunki uskey instance ke liye kuch nahi likha hein
emp1.showDetails()                   # ye bhi ek heen cheez hein

emp2 = Employee("Rohan")
emp2.showDetails()                   

'''
Par differece kya hein  , par 16th waley line mein 'showDetails' is not taking a Positional Argument 
and 17th waley line mein it is taking a Positional Argument                                  
'''