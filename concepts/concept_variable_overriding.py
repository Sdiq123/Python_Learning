'''
Variable overriding in Python, primarily occurring within the context of inheritance, 
is the technique where a subclass (child class) defines a variable or attribute with the same name as one inherited 
from its superclass (parent class). This allows the child class to provide a specialized value for an attribute, 
effectively replacing the parent's default value for that specific child class

The Concept of Variable Overriding

*) Inheritance Mandatory: Overriding requires an "is-a" relationship (inheritance).
*) Shadowing Behavior: The variable in the subclass "shadows" or hides the parent’s variable when accessed via an instance of the subclass.
*) Method Resolution Order (MRO): When looking up an attribute, Python checks the instance first, then the class, and then upward through parent classes. The first match found is used
'''


class Parent:
    data = (1,2,3,4)

class Child(Parent):
    data = (5,6,7,8)

    def combined_tuples(self):
        combined = self.data + super().data
        return combined 
    
c = Child()
print(f"Childs Data: {c.data}")
print(f"Combined Data: {c.combined_tuples()}")