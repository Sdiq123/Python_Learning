'''
Concept Of Immutability - jo Strings hein vo Immutable hotey hein
tum unko change nahi karsaktey, aisa nahi hein ki tum unko change nahi karsaktey, but inplace change nahi karsaktey 

'''

a = "!!!!!Sadiq!! !!!!! !!!Sadiq"         # a - jo bangayi vo bangayi main a ko change nahi karsakta , but a ki copy banasakta hun
print(len(a))        
print(a.upper())    # to ek nayi string milti hein mujhey. jismey saarey ke saarey letters hein vo uppercase ke hotey hein

print(a.lower())    # ye hamari string ko lower case mein convert karega
# Kya ye ek nayi String Banadega, nahi ye hamrey existing String ko nayi string mein convert kardega
# To basically ki string ke methods kya kartey hein, hamarey existing strings ke upar operate kartey hein aur ek nayi string return kartey hein


print(a.rstrip("!"))       # ye trailing characters ko remove kardeta hein 
# ye basically right side ke trailing characters ko nikaldeta hein  

print(a.replace("Sadiq","Pasha")) # Replaces all Occurences of a string with another string

'''
split() - Method in Python 
ye basically list mein convert kardeta hein 
agar string mein whitespaces hon to heen ye kaam karega, warna kaam nahi karega
'''

print(a.split(" "))

'''
capitalize(): -> this method is not there in Java Script
String ke Starting character ko Hamesha Uppercase karega aur baaki sarey characters ko LowerCase karega
Agar peley se starting character uppercase ho to kuch effect nahi hoga
'''
blogHeading = "introduction TO JS"
print(blogHeading.capitalize())


'''
centre(): -> Ye string ko centre mein align kardega as per the parameter given
starting mein to ye string ki lenth 25 thi, par baadmey iski length 50 hogayi - basically iski length badadi 
'''
str1 = "Welcome to the Console!!!!!!!"
print(len(str1))
print(len(str1.center(50)))

'''
count() : given a single character in a string kitni baar ek string repeat kar raha hein, count() usko bolta hein 
'''
print(a.count("Sadiq"))

'''
endswith() :check karega a ki ek particular string ek value ki hisab se end hogi ya nahi
ye boolean data tyoe mein value ko return karkey dega , jo ki main if-else waley loop mein aaram se use karsakta hun

-> we can also check for a value in-between the string by providing start and end index positions

'''

print(str1.endswith("!!!"))

print(str1.endswith("to",5,10))

'''
find() - Search karta hein for the First Occurence of a Index jahan par vo maujood ho
       - Agar aapki string nahi milti to vo -1 (minus) mein return karta hein
'''

str1 = "He's name is Dan.He is an honest man."  # Yahan par observe karna str1 do jagah defined hein, but string immutable hein kyun , kyunki python mein veriable override hosakta hein 
print(str1.find("is"))
# print(str1.find("iskkk"))


'''
index(): ye method same hein find() method ki tarah heen , agar same cheez jo mainey find() ke saath kari hein vo index() ke saath karun to mujhey exception miljayega
Agar ham chahtey hein ki hamara programme error dekey exit hojaye to ham index use karsaktey hein

Error ayega - "Value Error - substring not found"
'''
print(str1.find("iskkk"))


'''
isalnum() - If the Characters contains Alpha Numeric Characters A-Z,a-z,0-9 then it returns True , else it returns False
'''

str1 = "WelcomeToTheConsole!@@##$"
print(str1.isalnum())

'''
isaplha() - only aplhabets -> a-z, A-Z returns True else returns False 
'''

str1 = "Welcome00"
print(str1.isalpha())


'''
islower() - To Check Whether all the Characters mentioned or present are lower
'''

str1 = "Hello world"
print(str1.islower())

'''
isprintable(): - Returns True if all the characters in the given string are printable else returns False 
'''

str1 = "We wish you a Merry Christmas\n" # yahan par \n is not a printable character isilye False print karega
print(str1)
print(str1.isprintable())


'''
isspace() - returns true if the string conatins a space else returns flase
'''

str1 = "          " # using space bar
print(str1.isspace())
str2 = "            " # using Tab
print(str2.isspace())

'''
istitle() - returns True only if the First Letter of each word of the string is a uppper case else returns False
'''

str1 = "World Health Organization"
print(str1.istitle())

'''
swapcase() - Upper Case ko Lower Case mein convert karta hein aur  Lower Case ko Upper Case mein Connvert karta hein
'''

str1 = "Python is a Interpreted Language"
print(str1.swapcase())

'''
title() - Capitalize each word within the string
'''

str1 = "His name is Dan. Dan is a Honest Man"
print(str1.title())