''' 
Python main sabkuch ek Object hota hain
* Dictionary ek object hein
* Boolean ek Object hein
* Integer ek Object hein

'''




'''
        VARIABLES AND DATA TYPES IN PYTHON 

Variables - Variables bilkul ek container ki tarah hotey hain 

Ek COntainer main ham kai tarah ke cheezein daal saktey hain 
isi tarah ye containers main ham data ko store kartey hein 

Ye Data Memory main yani RAM main Store hota hein 

Data types - containers main aap kai tarah ke cheezein store kar saktey ho, isiko boltey hein data types 
ye container kis tarah ka hota hain ? Ye container memory ka hota hain 


Variables main ham kisisbhi tarah ke data types ko store karsaktey hain

Data Types Kyun Chahiye ?
-> Data Types Isliye chahiye kyunki ham alag alag type ke values ko variables main store karsaktey hein memeory ke RAM Mein

-> Data Types Kyun Chahiye taki ham variable ke upar operations karsakey without any error
'''

a = 123
b = True
print(a)
a1 = 9.1
c = "Sadiq"
print(b)
print(a+a1)
print("The Type of a is", type(a))
print("The Type of b is", type(b))
print("The Type of c is", type(c))

print("--------Numeric Data Types-----------")
a = 123
print("The Type of " ,a ,"is", type(a))

a1 = 9.1
print("The Type of" ,a1, "is", type(a1))

a2 = complex(2,8)
print("The Type of", a2 ,"is", type(a2))

print("-----Text Data : Str--------")
b = "Hello World!"
print("The Type of", b, "is", type(b))

print("-----Boolean Data--------")
c=True
print("The Type of", c ,"is",type(c))

print("-----------------------Sequenced Data : List, Tuple-------------------------")

''' 
-------LIST--------
List Kya Hota Hain - Ordered Collection Of Different Data Types hota hain

List is basically a list of Items jo ki alag alag data types se banta hein 

List is Mutable
'''
list1 = [ 5, 2.3, [-4.5,6],["Apple","Mango","Banana"]]
print("Type of List",list1,"is Type",type(list1))


'''
-------TUPLE--------
Exactly the same thing ye bhi Ordered Collection heen hain, just that ek baar hamney TUple Banadiya, phir ham Tuple ko Change nahi karsaktey 

aur tuple keelements ko paranthesis ke andar likhtey hein
'''

tuple1 = (("parrot" , "sparrow"), ("Lion", "Tiger"))
print("Type of tuple1",tuple1,"is Type",type(tuple1))



'''
--------Dictionary----------

-> Dictionary UnOrdered Collection of key value pairs 
-> Dictionary mein main kuch bhi store kar sakta hun , bachhey ka naam aur uskey kitney marks aaye  
-> Aur Dictionary ko Curly Brackets main Liktey hein
'''

dict1 = {"name":"Sadiq", "age":24, "canVote":True}
print("Value Of dict1 is:",dict1,"and type is :",type(dict1))


