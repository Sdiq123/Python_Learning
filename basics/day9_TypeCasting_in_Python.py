'''
----------TYPECASTING IN PYTHON-------------
maanlo ki hamney ek string variable likha hein aur uskey andar 27 likha hein double quotes ke andar , jab ham isko 3 without quotes ke saath add karengey to 
obviously hamey 30 nahi milega, kyun nahi milega kyunki 27 ek string hein isilye 

Magar hamey batana hein ki python ke andar jo hamney likha hein vo ek valid string hein to hamey usko typecast karna padega by using an int function 

'''

a = "1"
# a = "1Harry" ye error throw karega , jo aap TypeCast karna Chahtey ho agar vo ek valid integer to heen type cast possible hein aur dusrey varible ka bhi data-type same hona chahiye
# b = "2"  , Idhar a+b is not valid kyunki a ka data type alag hein aur b ka datatype alag hein
# a = 1
b = "2"
# b = 2

print(int(a)+int(b))

'''
Two Types Of TypeCasting

1. Explicit TypeCasting - Main Chahraha hun Convert karney ke liye, usey boltey hein Explicit

2. Implicit TypeCasting - Python Khud TypeCast Kardega , isey boltey hain implicit

'''


# Implict TypeCasting

c = 1.9
d = 8

#  Check the Respective .md File it will be helpfull
print(c+d) # Here this will always give 9.9, why because float is a level 1 DataType