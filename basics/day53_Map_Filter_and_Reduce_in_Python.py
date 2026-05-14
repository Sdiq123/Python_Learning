'''
Aap logon ko Map Filter aur Reduce - Advance List Manipulation karney ke liye kai baar use karna padega

Map , filter , Reduce - sirf python main nahi hotey 

Aur sirf List Manipulation ke liye use nahi hotey 

These Functions are higher order functions as they take other functions as arguments

Function jab ek function ko as a argument leta hein to usey boltey hein higher order function

Map, Reduce, Filter - ye teeno ek function letey hein aur dusra letey hein iterable
'''

def cube(x):
    return x*x*x

print(cube(2))

l = [1, 2, 4, 6, 4, 3]  # agar mujhey har ek element ka cube chahiye to main kaisey karunga ?

'''
---------------Map In Python---------------
'''
#  Normal tarika for - loop lagakar

newl = []
for item in l:
    newl.append(cube(item))

print(newl)

# Map Use kar kar - Map Hamesha, Map Object return karta hein , isiliye hame usey hamesha list mein convert karna padega
# Map Function Efficiency Purposes ke liye return kiya jaata hein
# Map ka pehla argument hoga function ka naam, aur phir vo list ka naam jo aap har element par yahi function apply karna chahtey ho


newlmapped = list(map(cube,l))
print(newlmapped)

print("newl mapped without using map function")

newlmappedwithoutafunction = list(map(lambda x : x*x*x , l))
print(newlmappedwithoutafunction)

'''
-------------Filter---------------
jin jin values ke liye filter true return karega vo output hongi, warna nahi hongi

'''

# iskey liye aapko filter function banana heen padega

def filter_function(a):
    return a>2 

newnewl = list(filter(filter_function,l))
print(newnewl)

'''
------------Reduce-------------
ye bhi higher order function hein 
ye bhi function as a argument leta hein
par ye hame import karna padta hein
--> check in next python file 
'''


