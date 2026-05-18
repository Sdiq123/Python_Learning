'''
-----------------------------> Getters <-----------------------------------
Python mein aap Getters aur Setters bhi use kar saktey ho  
-> kisi bhi ek function ke return value ko ek Object ki property ki tarah use kar saktey hein aur usey set bhi karsaktey hein 

-> Ye Encapsulation ka bahut aasaan tarika hota hein ,Implementation aap se dhaki hui hein 
'''

class MyClass:
    def __init__(self, value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    '''
    Getter
    '''
    @property   # jab bhi aap ek property ka decorator lagatey ho function ke upar to vo ek 'getter' banjata hein
    def ten_value(self):
        return 10*self._value
    
    # obj.ten_value = 67 , --> you cannot set the value like this for a getter method , you have to set it 
    '''
    Setter 
    '''
    @ten_value.setter
    def ten_value(self, new_value):
        self._value =new_value/10
        

obj = MyClass(10)
obj.ten_value = 67
print(obj._value)
obj.show()