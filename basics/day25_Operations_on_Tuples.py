# Manipulating Tuples 
# Directly koi method nahi hein tuple ko manipulate karne ka 
# agar change karna heen hein, to pehley tuple ko list banana padega, phir list ko tuple banana padega 

countries = ("india", "russia", "spain","Iran","Oman","Poland")
print("Initial tuple without a change...",countries)
temp = list(countries)
temp.append("vietnam")   # add an item
temp.pop(3)              # remove an item
temp[2] = "Finland"      # Change an Item
# print("Temp is a List now",temp)
countries = tuple(temp)
print("Tuple after changed...",countries)


# Aap do Tuples ko Concatenate karsaktey ho without chnaging them , kyunki ham ek naya tuple bana rahey hein
countries1 = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")
countries2 = ("Vietnam", "India", "China")
southEastAsia = countries1 + countries2
print(southEastAsia)


#-----------------------------------------------------------
#-----------------Methods in Python-------------------------
# ----------------------------------------------------------

# count() - The count() method of Tuple returns the number of times the given element appears in the tuple.

Tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
res = Tuple1.count(3)
print('Count of 3 in Tuple1 is:', res)

# Ek Convention follow kartey hein ki jo classes likhtey hein ham, vo capital letter se likhtey hein aur jo variables likhtey hein vo small letter se shuru hotey hein 

# Index Method in TUple

# The Index() method returns the first occurrence of the given element from the tuple.
# Note: This method raises a ValueError if the element is not found in the tuple.
# Syntax - tuple.index(element, start, end)

Tuple = (0, 1, 2, 31, 2, 3, 1, 3, 2)
res = Tuple.index(3)
res = len(Tuple)

# res = Tuple.index(311)  # raises value error
res1 = Tuple.index(3,4,8)
print('First occurrence of 3 is', res1)


