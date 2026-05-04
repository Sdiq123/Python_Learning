#  TUPLES
#  Tuples bhi lists ki tarah heen hein par Tuples ko aap kabhi bhi change nahi karsaktey 
#  Tuples are unchangebale you cannot change them once after creation

tup =(1,2,76,342,32,"green")
print(type(tup),tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

# --------> Ask Rohith <----------
# Agar sirf ek heen Tuple ko print karna hein to kya karengey , tup=(49) ya tup=(49,)

# Positive Indexing aur Negative Indexing, Python main same hoti hein , aap ek baar lists check karsaktey ho
 
print(tup[-4])

# Check for an Item 
if 342 in tup:
    print("yes 342 is present in tuple")
else:
    print("No 342 is not present in tuple")
    
#  Slicing Jaisey hamney kari Lists mein , Same waisey heen Tuples main bhi karsaktey hein 
#  Slicing Karney ke baad ek naya Tuple Return hojata hein

tup2 = tup[1:4]
print(tup2)     # yahan tup change nahi hoga , jo bhi chnages hongey vo ek naya variable banakar de dega  

# List Ke saarey Methods ek baar dekh lo Tuple main , farak sirf itna hein ki Tuple aapney ek baar banadiya phir change nahi karsaktey

# Tuples are Immutable
# Strings are Immutable 
# Lists are Mutable