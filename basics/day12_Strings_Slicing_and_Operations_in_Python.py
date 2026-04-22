'''
Real Life mein ginti hamesha 1 se shuru hoti hein, par programming mein ginti hamesha 0 se shuru hoti hein ye yaad rakho 
String Basically Array ki tarah hoti hein, Sequence of characters hoti hein 

Functions Ke liye Ham Paranthesis use kartey hein 

[] ham hamesha indexing aur slicing ke liye use kartey hein 
'''

names = "Harry,Shubham"
    # =  0123456789101112
    # =  Harry,Shub h a m 

print(names[0:5]) # ye hamesha [0:n-1] tak heen print karta hein , is ney 5th position ke element ko print nahi kara 

print(len(names)) # Length hamesha Count hogi, idhar length 12 nahi 13 hogi

fruit = "Mango"
print(fruit[0:4]) # Including 0 but not 4 , ye 0 se lekar 3rd index tak heen print karega
print(fruit[:4]) # Agar mujhey zero nahi lagana hein starting mein to python khud zero ko assume karlega
print(fruit[1:4]) # Agar mujhey 1 se chahiye to main kya karunga, 1 se likhunga
print(fruit[:]) # AGar main Kuch na Likhun end main to Python khud length lagalega
# Negative Slicing 

print(fruit[0:-3]) # Negative Slicing ko Python is tarah interpret karta hein
# print(fruit[0:len(fruit)-3])
# print(fruit[0:2]) -> to ye sirf 0 aur 1 ki index position tak heen print karega 

print(fruit[-1:-3]) # It gives nothing 5-1 = 4 , 5-3 = 2

print(fruit[-3:-1]) # Idhar ye print(fruit[2:4]) 2nd index se lekar 3rd index tak print karegi

len1 = len(fruit)
print(len1, "letter word")