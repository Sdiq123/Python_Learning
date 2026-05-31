'''
Walrus Operator - New Addition after 3.8 and it makes easy to work 
dekhtey hein kya kya cheezein hein jo easy banata hein 
'''
# agar aap kisis dusri language se aa rahein hein to aapko pata hoga ki aap within a expression heen assignment kar saktey ho 

# Python mein shuru se heen ye dikkat hua karti thi aur iski wajah se kaafi dikkat 

'''
Walrus Operator is nothing but, ek expression ke within rehtey hue assignment karsaktey hein 
'''

# walrus operator ka syntax ( := )
# Allows to assign a value to a variable in a expression 

a = True
print( a:= False)

numbers = [1,2,3,4,5]

while( n := len(numbers) ) > 0:
    print(numbers.pop())


# walrus operator :=

# new to Python 3.8
# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

happy = True
print(happy)

print( happy := True)


#----------- without walrus operator
# foods = list()
# while True:
#     food = input("What food do you like ?: ")
#     if food == "quit":
#         break
#     foods.append(food)

foods = list()
while (food := input("What food do you like? : ")) != "quit" :
    foods.append(food)
