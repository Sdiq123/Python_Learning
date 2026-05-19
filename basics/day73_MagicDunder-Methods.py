'''
----> Magic Methods jinhey Dunder Methods bhi Boltey hein <----------
ye special methods hotey hein jo ki double underscore se start hotey hein aur double underscore se end hotey hein

kya aapney kabhi __len__ ko call kiya hein ? nahi par aapney len() ko zarur call kiya hoga

Magic Methods Basically Classes mein defined hotey hein aur inka purpose hota hein kuch special kaam karna

init - Method ek naya method hein jo bhi kisi bhi class ke naye Instance ko initialize karta hein
'''

from emp import Employee
    
    
    
e = Employee("Sadiq")
print(str(e))
print(repr(e))      # ye cheez observe karna kya hamney underscore se call kiya usko? nahi , par phir bhi hamey answer mil raha hein
# print(e.name)
# print(len(e)) # ye cheez error dega ki 'Employee' has no len() , par jab main __len__ function ko define karunga tab mujhey ye kaam easy hojayega
e()