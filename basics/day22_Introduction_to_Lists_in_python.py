'''
        LISTS IN PYTHON
Agar aap log ek particular entity main bees se adhik cheezein store karna chahtey ho to Lists banatey ho
List of marks of students of class8
List of people living in Europe

In saari cheezon ke List banakar aap inpar operations kar saktey hein, unko iterate karsaktey hein, aur unko ek naam se pukar saktey hein

List bananey se ham cheezon ko ek category ke andar collect karsaktey hein
'''

# List are oredered collection of data items , matlab inka order maintain rehta hein, inka order change nahi hota
# They store multiple items in a single variable
# List items are separated by commas and enclosed within square brackets []
# Lists are changebale meaning we can alter them after creation


marks = [3,5,6]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(marks[2])

#  In a single variable of list we can also store different data types that is int , string and boolean

marks = [3, 5, 6, "Harry", True, False, 6, 7, 2, 32, 345, 23]
# index=[0, 1, 2,   3,       4,    5  ]
# Index alag hoti hein aur length alag hoti hein - length hameah 1 se shuru hoti hein

print(marks[3])
print(marks[4])
print(marks[5])

# Negative Indexing --> kabhi bhi negative index miljaye , usey pehley positive index main convert kardo length lagakar 
print("Negative Indexing")
print(marks[-3]) # this is nothing but len(marks)-3 ==> 6-3 ==> 3 ==> print(marks[3]) ==> Harry 

if "Harry" in marks:              # in keyword ka istemaal karkey aap dekh saktey ho 
        print("Yes")
else:
        print("No")
        
        
if "arry" in "Harrry":                # Same things are applied for strings as well !
        print("Yes arry is there")
else:
        print("No arry is not there")
        
        
#  Agar mujhey saarey marks print karwana hein to ?
# Concept of Jump Index

print(marks)
print(marks[:]) # yahan python aisa kaam karega -> print(marks[0:len(marks)])
print(marks[:])         # saarey ke saarey marks print hojatey hein 
print(marks[1:])        # ye 1 se start hokar saarey elements tak 
print(marks[1:-1])      # first covert thus in positive index => marks[1:5] => ye 1 se start hoga 4th index tak print karega aur 5 included nahi hoga
# Jump Index
print("printing... Jump Index")
# marks = [3, 5, 6, "Harry", True, False, 6, 7, 2, 32, 345, 23]
print(marks[1::2])     # marks[start:end:jump] => 1 se 3 tak print karega with the difference of 2 
print(marks[:12:2])
print(marks[1:12:2])


# LIST COMPREHENSION
# ---> Aap ek naya list bana rahey ho , during printing or while the programme is running 


print("printing........List Comprehensons")

lst = [i for i in range(5)]
print(lst)

# Agar main chahun to ek list se dusra list bhi bana sakta hun, list ko iterate karke 
lst = [i*i for i in range(10) if  i%2 == 0]
print(lst)