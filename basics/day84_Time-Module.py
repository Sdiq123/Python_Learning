'''
Time Module in Python - Built in Module , jo hamey bahut saarey time related operations karney mein madad karta hein

'''
import time

def usingWhile():
    i = 0
    while i < 5000:
        i = i + 1
        print(i)

def usingFor():
    for i in range(5000):
        print(i)

init = time.time()  # returns the time in seconds epoch is a point were the time starts
usingFor()
t1 = time.time() - init
print(t1)

init = time.time()  # returns the time in seconds epoch is a point were the time starts
usingWhile()
print(time.time() - init)

# sleep() - This is used to wait 

# strftime() - Time ko format karta hein as a string based on a specific format