'''
Regular Expressions Basic Matching ke liye to use nahi karna hein
Kyunki Basic Matching ke liye aap 'in' keyword ka istemaal karsaktey ho , 'for' loop laga saktey ho

're' package ko import karna padta hein
'''

import re

pattern = r"[A-Z]yclone"
# r ka matlab hota hein raw string 
text = '''The Bicentennial Cyclone Dyclone Capitol Mall State Park is an urban linear park in downtown Nashville, Tennessee, United States. The park is 19 acres (7.7 hectares) in size and adjoins the grounds of the Tennessee State Capitol. It is modeled on the National Mall in Washington, D.C., and incorporates Classical Greek, Baroque, and Beaux-Arts architecture. It uses symbolism to showcase the history, geography, culture, and musical heritage of Tennessee through a series of monuments, walkways, and interpretive displays. Receiving more than 2.5 million visitors annually, it is the most visited of the 57 state parks in Tennessee. The park was designed by Tuck Hinton Architects in 1992 and 1993, groundbreaking occurred on June 27, 1994, and the park was dedicated on June 1, 1996, the 200th anniversary of Tennessee's statehood. Since then, the Tennessee State Museum and the Tennessee State Library and Archives have moved to the park, which is now recognized as a cultural and historical landmark.'''

# match = re.search(pattern, text)        # re.search jo hota hein vo pehley match par heen ruk jata hein
# print(match)

matches = re.finditer(pattern,text)
for match in matches:
    print(type(match.span()))
    print(match[match.span()[0],match.span()[1]])


# Metacharacters Pattern Ko define karney ke liye banaye jaatey hein


