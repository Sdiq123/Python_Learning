'''
Ek Bahut heen Classic Error aata hein Python Mein 
Agar aap Module ke naam se File Banatey ho, to Python Module main nahi dekta hein , file main heen dekhta hein aur error aaney lagjata hein

Nested If-Else Kuch nahi Hein , Ek If ke andar aapney aur ek if Lagadiya
'''

num = int(input("Enter a Number: "))
if (num < 0):                       # Ye EK Level Of Indent Hogaya 
    print("Number is negative.")
elif (num >0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is greater than or equal to 20")
else:
    print("Number is Zero")