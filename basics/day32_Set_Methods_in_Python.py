'''
Set Methods
sets operations are the same way how we perform in Mathametics to...
'''
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2)) # jab main ye operation perform kar raha hun, tab mera s1 aur s2 untouched hein, inko kuch nahi hua hein
print(s1, s2 ) # yahan ye dono unvhnaged hein 
s1.update(s2) # iska matlab s1 ke andar s2 ke values bhi lado jo s1 main nahi hein



cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.union(cities2)
# print(cities3)

# cities4 = cities.intersection(cities2)
# print(cities4)

# intersection_update() - issey jo bhi common elements hein vo update hojayengi cities main
# cities5 = cities.intersection_update(cities2)
# print("Intersection_Updated_Cities",cities)

'''
Symmetric Difference = (A U B) - (A intersection B)
Matlab Kya hua - wo saari values jo common nahi hein do sets mein

'''

cities6 = cities.symmetric_difference(cities2)
print(cities6)

'''
difference() and difference_update() - prints only items that are present in the original set and not in both the sets
ye ek tarah se A - B hein 
'''

print("difference",cities.difference(cities2))

'''
isdisjoint() - check karta hein ki items of given set are present in aother set or not 

iska matlab hota hein ki ek dusrey se unka koi matlab nahi hota , koi bhi intersection unmey nahi hota

'''

print("disjoint",cities.isdisjoint(cities2))

'''
issuperset() - kya dusrey waley set ke elements pehley waley set ke andar hein ?

'''
print("Superset",cities.issuperset(cities2))

'''
issubset() - ye super set ka ulta hein

'''
print("Subset",cities.issubset(cities2))

'''
add() - agar ek element add karna chahtey ho to add() method ko use karo
'''
cities.add("Helsinki")
print("add()",cities)

'''
update() - If you want to add more than one item, update use kar saktey hein
'''

'''
remove() and discard() - both are used to remove items from the set 

remove() - agar element hein to remove kardega , agar nahi hein to error throw karega aur programme wahi ke wahi ruk jayega

discard() - ye agar element nahi hein to error thorow nahi karega aur programme ko execute karega
'''

cities.remove("Tokyo")
print("remove()",cities)


'''
pop() - this element removes the last element of the set but the catch is that we dont know which item gets popped as sets are unordered

'''
item = cities.pop()
print(cities)
print(item)

'''
del() - This is not a method, this is a Keyword , which deletes the entire set 

'''

# del cities
# print(cities)

'''
Clear() - what if we dont want to delete the entire set , we just want to delete all the items in a set

'''
cities.clear()
print(cities)