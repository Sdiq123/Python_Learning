'''
For - Loops 

kai baar kai aisey kaam hotey hein jo hamey repeat karney padtey 
roz subah utkey hein office ke liye ready hotey hein 
roz subah utkey paani ki bottle bhar kar , har ek bottle fridge mein rak tey hein

Looping ka concept Python Programming ko bahut zyada Strong Banata hein aur Programmer ka kaafi samay bachata hein 

Sometimes a programmer wants to execute a group of statements a certain number of times. This can be done using loops. Based on this loops are further classified into following main types; 
- for loop
- while loop 

For Loop 
for loops can iterate over a sequence of iterable objects in python. Iterating over a sequence is nothing but iterating over strings, lists, tuples, sets and dictionaries.

Python ke andar kuch Iterable Objects hotey hein jinko ham Loop karsaktey hein
List ke andar ke har ek element ko bhi loop karsaktey hein
String ke andar ke har ek element ko bhi loop karsaktey hein
aisey jitney bhi data types hein python mein uskey har ek element ko access karsaktey hein
'''

# name = 'Abhishek'
# for i in name:   # Ek - EK karkey i ki value A se lekar K tak jayegi
#     print(i)
#     if(i =='b'):
#         print('This is something special!!')

# colors = ["Red", "Green", "Blue", "Yellow"]
# for x in colors:
#     print(x)     # yahan main x ko bhi iterate karsakta hun
#     for i in x:
#         print(i)
        
'''
range() - range kya hein 

'''
# range() - with single parameter
for k in range(5):   # range(5) - matlab 0 se lekar 4 tak jayega, matlab n-1 tak jayega
    print(k)         # Magar Mujhey 1 se lekar 5 tak print karna hein koi baat ni k+1 kardo 1 se lekar 5 tak print hojayega
                     # Agar aap ko 2 se lekar 6 tak chahiye to k+2 kardo hojayega
                                 
#range() - with double parameter                                #  
                                         
                     # range() - Function ke andar bhi aap apney arguments paas karsaktey ho 
for k in range(1,9): # k ki value idhar 1 se lekar 8 tak jayegi 
    print(k)
    
#range(start, stop, step) - with tripple parameters

for k in range(1,15,2): # yahan k ki value 1 se start hogi , 1+2 =3 , 3+2=5 .....aisey kartey jitney numbers 15 ke andar possible hein unhey return karegi , uskey baad stop kardegi
    print(k)            # for( i=0, i<=15, i++) this is equivalent to for k in range(1,15,2)

