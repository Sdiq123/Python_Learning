'''
DocStrings , Madad karti hein ek function ko easily samjney ke liye, Agar aap ko vo function description ke saath miljaye to obviously achha rahega 
Python Doc strings are the string literals that appear right after the definition of the function. method, class or module

ye comment se kaisey different hoti hein dekhengey


'''

def square(n):
    # print(n**2) - To agar ye line of code main yahan likhdun to kya docstring kaam karega, nahi obviously nahi, kyunki docstring hamesha just function ke neechey heen likhtey hein 
    '''
    Takes in a number n, returns the square of n
    '''
    print (n**2)

square(5)   # If you hover on this function name square, then you obviously get a explanation of what exactly it this function going to do

print(square.__doc__)   # From this you can print the doc string itslef , ya phir main doc string ko parse karsakta hun

# Docstrings are not comments, ye string aapko just function ke body ke upar hamesha daalna hoga

# =======================================================================================================================================================================================
# ----------------------------------------------------------------------------------------------PEP 8-----------------------------------------------------------------------------
# =======================================================================================================================================================================================

# PEP 8 ek guideline hein aur best paractice provide karta hein python code ki 

# PEP (Python Enhancement Proposal) - 2001 ek main Guido Van Rossum, Barry Warsaw, and Nick Coghlan ne is isko likhi thi 

'''
Zen Of Python
'''

#  Type import this in your terminal and a python poem comes which is very relatable
