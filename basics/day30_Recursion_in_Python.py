'''
----------------- Recursion In Python ---------------------------

Recursion basically Functions heen hotey hein , Ek Function ke andar usi same function ko call karney sey usey recursion kahtey hein

'''

# Factorial(7) = 7*6*5*4*3*2*1 
# Factorial(6) = 6*5*4*3*2*1 
# Factorial(5) = 5*4*3*2*1 
# Factorial(4) = 4*3*2*1 
# Factorial(3) = 3*2*1 
# Factorial(2) = 2*1 
# Factorial(1) = 1 
# Factorial(0) = 1          ----> Important

# factorial(n) = n * factorial(n-1)     --> Iss Information ko use karkey kya main recursively function ko call kar sakta hun ? yes 

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(3))
print(factorial(4))
print(factorial(5))

# ye kaam kaisey kar raha hein 
# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)
# 5 * 4 * 3 * 2 * 1

'''
Another Famous Example of Recursion is Fibonacci Series

f0 = 0
f1 = 1
f2 = f1 + f0
.
.
.
.
f(n) = f(n-1) + f(n-2)

'''
n = 10
a = 0
b = 1

for i in range(n):
    print(a)
    next_number = a + b
    a = b
    b = next_number
    

     