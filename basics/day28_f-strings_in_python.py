'''
f-strings ek aisa tarika hein jo strings ke andar variables ko conveniently induce karsakta hein
aur ye feature python 3.6 se dekhney ke liye milta hein

f-string use hoti hein --> string formatting ke liye use hota hein f-strings

string formatting karney ke time par jo problem ho rahi thi vo solve karney ke liye python ne f-strings ki feature nikali
'''

# Problem jo actually ho rahi this, is method mein kuch kharabhi nahi thi , but ye method convenient nahi tha bus 

'''
letter = "Hey my name is {1} and I am from {0}"
country = "India"
name = "Sadiq"

print(letter.format(country, name))
'''

country = "India"
name = "sadiq"

print(f"Hey my name is {name} and i am from {country}")

txt = "For only {price:.2f} dollars !"  # ye sirf 2 decimal places tak heen apni value lega
print(txt.format(price = 49.09999))

# same cheez agar mujhey f-strings ke madad se karni hein to main aisey karunga 
price = 49.0999
txt1 = f"For only {price:.2f} dollars !"  # ye sirf 2 decimal places tak heen apni value lega
print((txt1))

# agar aap ek string ki value 60 karna chahtey ho to 
print(type(f"{2*30}"))

'''
One Important thing, If I need to show the Variable in the f-string as it is, then i have to enclose it with double curly braces {{}}, so that the variable will
not get substituted with the value of the variable
'''
print(f"Hey my name is {{name}} and i am from {{country}}")

