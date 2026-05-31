'''
Multiple Inheritence - multiple parent classes se ek child class inherit karey to, usually do classes dekhney ko miltey hein
'''

#  class ChildClass(ParentClass1,ParentClass2,ParentClass3):
    
class Employee:
    def __init__(self,name):
        self.name = name
        
    def show(self):
        print(f"The name is {self.name}")

class Dancer:
    def __init__(self,dance):
        self.dance = dance
    def show(self):
        print(f"The dance is {self.dance}")

class DancerEmployee(Dancer, Employee):
    def __init__(self,dance,name):
        self.dance = dance
        self.name = name
        
o = DancerEmployee("Khathak" , "Shivani")
print(o.name)
print(o.dance)
o.show()

'''
Special Method In Python - MRO ( Method Resolution Order )

'''
print(DancerEmployee.mro())