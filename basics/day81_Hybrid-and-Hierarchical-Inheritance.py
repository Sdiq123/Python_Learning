'''
Hybrid Inheritence - Ek se zyada Inheritence Use kartey hein to 

'''

class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3(Derived1, Derived2):
    pass


'''
Hierarchial Inheritence - Multiple Subclasses Inherit from a single Base Class
        CEO
         |
    -------------
    |    |      |
    m1   m2     m3
'''

class BaseClass:
    pass

class D1(BaseClass):
    pass

class D2(BaseClass):
    pass

class D3(D1):
    pass