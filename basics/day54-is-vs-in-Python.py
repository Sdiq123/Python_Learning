'''
'is' aur '==' dono comparison operators hotey hein 
python mein 'is' keyword hein jissey hamey pata chalta hein ki if a variable is 'None' or not  
'==' operator bhi hota hein jo ki kaafi similar hota hein 
'''

# 'is' compare karta hein exact location in the memory ko aur 
# '==' compare karta hein values ko  

a = 4
b = "4"

print(a is b) #False
print(a == b) #False

c = [1, 2, 43]
d = [1, 2, 43]

print(c is d) #False 
print(c == d) #True

e = 3   # 3 ek constant hein immutable hein to python ek aur memory location waste nahi karega, dusrey 3 ko dusrey memory location mein nahi dalega, aur isiko leverage karlega
f = 3

print(e is f) #True   #ye case sirf immutable cheezon pe hoga jaisey constant , string and tuple
print(e == f) #True

# 'is' operator identity ko compare karta hein

g = (1,2,3)
h = (1,2,3)

print("Checking Immutable variables",g is h)   #True
print("Checking Immutable variables",g == h)   #True