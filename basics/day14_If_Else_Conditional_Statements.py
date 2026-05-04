'''
if 
elif
else

kayi baar programme mein hota hein ki main condition ke hisab se kaam karunga

'''

a = int(input("Enter your Age: "))
print("Your age is:",a)
# Conditional Operators: > , < , >= , <= , == , !=
'''
Ye conditions par evaluate hogi aur Hamesha Boolean Main Output ko Return karegi
'''

# print(a>18)
# print(a<=18)
# print(a==18)
# print(a!=18)

if (a>18):                      # yahan paranthesis main hamesha condition lagegi
    print("You Can Drive")      # Aur colon kyun lagraha hein, isey boltey hein Indentation, jissey pata chalta hein ki ham vo block of code ke andar hein
    print("yes")                # Agar Evaluate/return True karega condition to if ke andar aata hein warna else ke andar chalajayega
else:
    print("You Cannot Drive")
    print("No")
print("Yay!!")                  # ye aakey hamesha else ke bahar hein to hamesha bhaley heen is wala block chaley ya else wala block chaley ye to hamesha print hoga