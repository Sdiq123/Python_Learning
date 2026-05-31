'''
Generators ka use hota hein Python mein on the file value ko generate mein

Generators are different from Lists , Lists ke andar pehley se value ko rakhi hoti hein, lekin "Generators" on the fly value ko generate kartey hein

Generator Function ek Generator Object ko return karta hein

Speciality ye hein ki, ye values ko store karkey nahi rakta, par value ko on the fly bananey ka code store karkey rakha jaata hein
'''


def my_generator():
    for i in range(5):
        yield i
        
# yield keyword ek Generator ko return karta hein , aur execution ko suspend kardeta hein jab tak tum next value request nahi kartey 

# Ask ROHITH - what is the use of yield statement, ANSWER - yield is always used to generate values on the fly
# Jab bhi aap yield statement dekho to samaj lena ki aap ek Generator Function ke andar ho

gen = my_generator()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
