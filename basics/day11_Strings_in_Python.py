'''
Python mein kisibhi cheez ko double quotes ya single quotes ke andar daal do to vo string banjaati hein 

Basically Strings are like a Character Array 

Python Strings are "like an Array Of Characters"- But Strings are not an Array, to phir Array ke kya matlab hua - collection of Items  
'''

name = "Harry"  # Yahan par name jo hein vo ek sequence of characters hein 
# Aur Yahan Ye Characters Indexed Hein"
# Programming mein jo index hoti hein, in most of the proh=gramming languages vo zero se start hoti hein

# name  = "Harry"
# Index = "01234"

print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])


# friend = "Rohan"
# anotherfriend = 'Lovish'


'''
Looping through the Strings

'''

apple = ''' He Said, 
Hi Harry 
Hey I am Good
"I want to eat an apple
'''
#  Agar Mujhey is string ke saarey characters ek ek karkey print karwaney hein to main kaisey print karwaunga?
# To Haan Jawab hein ki for loop 
 
print (" Printing through a For Loop")

for character in apple:
    print(character)



sentance = "He said, \'I want to eat an apple\'."
print(sentance)

sentance2 = 'He Said, "I want to eat an Apple".'
print(sentance2)



'''
Multi Line Strings In Python 

-> Agar Tumhein MultiLines print karni hein Python main, to ya to tripple single quotes use karengey ya phir tripple double quotes 

'''

s2 = """Hello Sadiq , 

How Are You, Hope You are Enjoying Learning Python"""

print (s2)