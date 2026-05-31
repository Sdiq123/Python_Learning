'''
Most of the inheritence jo dekhtey hein vo single inheritence heen dekhtey hein
'''
#  class ChildClass(ParentClass)

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")
        
class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
        
    def make_sound(self):
        print("Bark!")
        
d = Dog("golden","dog")
d.make_sound()


a = Animal("german","shepherd")
a.make_sound()

