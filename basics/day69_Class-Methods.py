'''
Class Methods ko ek Class ka Reference lekar kya milta hein ?

Class is a way to create Custom Data Types

Class Methods are always Bound to the Class and not to the Instance of the class
'''

class Employee:
    company = "Apple"
    # koi bhi method jo hein vo instance ke liye banta hein class ke liye nahi banta
    def show(self):
        print(f"The name is {self.name} and company is {self.company}")

    '''
    usually jo functions mein aap likhtey ho vo self , se likhtey , magar aapko class variables change karna hein to aap 'classmethod' - decorator ke saath self use nahi karsaktey, aap uskey siwa kuch bhi use karsaktey ho   
    '''

    @classmethod       # ye decrator directly class ke andar edit kaney mein madad karega
    def changeCompany(cls, newCompany): # yahan main 'cls' ki jagah kuch bhi likh sakta tha , sadiq, harry , gobi, tindi , ya kuck bhi matter nahi karta, kyunki vo jo bhi higa object mein uthakar de dega
        cls.company = newCompany

e1 = Employee()
e1.name = "Sadiq"
e1.show()
e1.changeCompany("Tesla") 
e1.show()

print(Employee.company) # ye hamesha Apple heen print karega tesla nahi Print karega, kyunki us particular instanc ko change kara class variable ko nahi

'''
ye Decorator - '@classmethod' Add  karney ke baad heen , aap class Variable ko edit karsaktey ho warna edit nahi karsaktey
'''