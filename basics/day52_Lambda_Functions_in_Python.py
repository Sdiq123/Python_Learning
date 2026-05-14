'''
Lambda Functions use hotey hein bahut saarey Anonymous Functions likhney ke liye
Anonymous Function - yaniki ek aisa function jiska naam nahi hota aur sirf ek expression hota hein

Lambda Functions are single expressions
'''

# def double(x):    # normal way of writing functions
#     return x*2
# lamda functions kab use karna hein jab aapko one liner use karna hein

double = lambda x:x*2   # yaniki ek function ka variable banadiya aur usi ko as a function use karliya 
cube = lambda x:x*x*x
avg = lambda x,y:(x+y)/2
avg3 = lambda x,y,z:(x+y+z)/3

print(double(5))
print(cube(5))
print(avg(5,7))
print(avg3(5,7,9))

# asli use case lambda functions ka tab use aata hein jab aap function ko as a  argument pass kartey ho
# Confuse mat hona kya aap ek function ko as a argument pass karsaktey hein ? --> yes pass karsaktey hein
# kya aap ek function ko function pass karsaktey hein - yes pass karsaktey hein

def appl(fx, value):
    return 6 + fx(value)

print(appl(cube,2))

#----------> one liner instead of all this <----

print(appl(lambda x: x * x * x, 2))