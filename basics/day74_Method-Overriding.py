'''
---> Method Overriding <-----
Ye ek tarika hota hein child class ke andar Parent Class se jo Method aaya hein usey change karney ka
is tarah se aap ek Method ko Override karsakta python ke andar chaliye dekhtey hein
'''

# Method Overriding ham tab kartey jabhi hamko ek Parent Class ke Method ko child class ke Hisab se modify kartey hein

'''
Method Overriding is a Powerful feature in Object Oriented Programming
'''

class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x * self.y
        
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):     # here you are changing the method area 
        return 3.14 * self.radius * self.radius
                #or
        #return 3.14 * super().area()
        
rec = Shape(3, 5)
print(rec.area())

c = Circle(5)
print(c.area())