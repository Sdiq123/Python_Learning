'''
Hamey Use karna Hain Time Module ka and Depending on the Time hamey user ko greet karna hain whther it is Good Morning, Good AfterNoon, Good Evening and Good Night
'''

# Hint for the Programme

import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
timestamp = int(time.strftime('%H'))
print(timestamp)
# timestamp = time.strftime("%M")
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)


if (timestamp < 12 ):
    print("Good Morning Sir ! ")

elif (timestamp >=12 and timestamp <=15):
    print("Good AfterNoon Sir")
    
elif (timestamp >15 and timestamp <= 18 ):
    print("GoodEvening Sir !")
    
else:
    print("Good Night !")
    
# https://docs.python.org/3/library/time.html#time.strftime