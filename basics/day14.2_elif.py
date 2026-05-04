'''
Maanlo Mujhey ek se Jyada Statements Execute Karwani hein based on Conditions to main elif wali condition lagaunga

ye kaam kaisey karta hein, sabsey pehley if ki condition check hogi , agar if ki condition True hogayi to vo block ke andar ka code execute hoga
Agar nahi Match hui to elif ke saary conditions ko one by one check karega, phir last mein else wali condition ko execute karega agar koi condition match na ho to 
Agar Koi Condition match hogayi to else ke bahar Ajayega Code 
'''

# applePrice = 210
# budget = 200
# if (applePrice <= budget):
#     print("Alexa, add 1kg Apples to the Cart")
# else:
#     print("Alexa, do not add Apples to the cart")

# elif Conditions

num = int(input("Enter the value of num: "))
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
elif (num == 999):
    print("Number is Special.")
else:
    print("Number is positive.")
    
print("I am Happy Now") # Ye Particular line of code ka if-else Ladder se koi matlab nahi hein

