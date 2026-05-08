'''
                                Sets In Python
Set is a Collection of well defined objects
Python mein agar aap ek aisa data type chahtey ho jismey repeated entries nahi ho to aap set bana saktey hein

Example - Maanlo aap ko ek list collect karna hein jinka naam S se shuru hota hein , maanlo duplicate entries exist karti hein to aap kaisey store karengey?
but duplicate entries mujhey nahi chahiye, to main isko kaisey karunga isilye set data type laya gaya hein python mein

'''

s = {2,4,2,6} # idhar 2 mainey duplicate kiya hein but still 2 screen par print nahi hoga
print(s)

# All the methods relevant to list can be done with sets, except for the fact that values can be repeated 

# ######## Sets are UnOrdered Collection Of Data Types 
# ######## Sets are Immutable , Sets donot contain duplicate items
# ######## Sets can contain different types of data types as well

info = {"Carla", 19, False, 5.9, 19}   # Unordered matlab, ye zaruri nahi hein ki pehley carla heen aayegi, uskey baad 19 heen aayegi , har ek print ke dauran kahi bhi , kabhi bhi kuch bhi a sakta hein jumble hokar print mein
print(info)

# Kyunki ye Order maintain nahi kartey, har print ke dauran , random tarikey print karengey , to aap inko index nahi karsaktey, also ye duplicate to allow nahi kartey

'''
 **Quick Quiz:** Try to create an empty set. Check using the type() function whether the type of your variable is a set
'''
l = {} # Kyunkii dictionary ka syntax bhi same hein start aur end flower brackets se hota hein, to ye empty set nahi, empty dict heen dega
print(type(l))

m = set() # ab ye hamara empty set hein
print(type(m))

# Access Kaisey Karengey aap set ke items ko - with the help of a for loop 

for value in info:
    print(value)        # ye aapko kisi bhi order mein dekhney ko milengey
