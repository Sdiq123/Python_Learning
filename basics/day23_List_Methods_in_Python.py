l = [11, 45, 17, 25, 49, 66,66,78,49,49,49]
print(l)
l.append(7) # append is a method jo ki at the end of this list 7 ko rak dega 
print(l)
# sort - sorts in Ascending Order 
print("Sorting....")
l.sort()
print(l)
l.sort(reverse=True)    # sorts in Descending Order 
print(l)
# Reverse Method - jo hamari original list hein usko ulta kardeta hein 
l.reverse()
print(l)
# Index Method - 
# This method returns the index of the first occurrence of the list item
print(l.index(11))
# Count Method - 
# Returns the count of the number of items with the given value 
print(l.count(49))

# copy() - returns the copy of the list without modifying the actual list
# ----------->Ask this Question to Rohith<----------------------
print("Copy() - Method")
# m = l
# m[0] = 96
# print("original list :",l)  # l also is changed , m also is changed , why because memory mein jo list bani hein vo ek heen hein aur vo hein l, to jab tum m ko chnage karogey to obviously l bhi change automatically hoga
# print("copied list :", m)

m = l.copy()
m[0] = 0
print("original list :",l)
print("copied list :", m)

# insert() - Method :- agar ek given index mein item ko insert karna chahtey ho 
l.insert(2, 899)
print(l)

# Concatenating Two Lists 
# -------> Type 1 
# extend()- This Method adds an entire list or any other collection datatype(set, tuple, dictionary) to the existing list.
# iska matlab hein ki m ko kholo aur l ke end main rak do
m1 = [900, 1000, 1100]
l.extend(m1)
print(l)

# -------> Type 2
# you can simply concatenate two lists to join two lists 
colors1 = ["voilet","indigo"]
colors2 = ["blue","green","yellow"]
colors = colors1+colors2
print(colors1+colors2)