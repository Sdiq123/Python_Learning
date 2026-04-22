'''
Short Cut to Replicate a line , this replicates a entire line 
-->Alt + Shift + Down 
'''




'''
Answer to the Calculator Question 
'''



'''
# ---------------My Thought Process and My Solution----------------------------

print("Universal Calculator")
n = int(input("enter a1 number to perform operation"))
m = int(input("Enter a2 number to perform the operation"))

ch = 0 
print("press 1 to perform Addition")
print("press 2 to perform Subraction")
print("press 3 to perform Multiplication")
print("press 4 to perform Division")
print("press 5 to perform Floor Division")
print("press 6 to perform Modulus")
print("press 7 to perform Exponenetial")

ch = int(input("Select a Choice to Perform the Operation"))

if ch == 1:
    print("Addition of",n, "and", m,"is",n+m)
    
elif ch ==2:
    print("Subraction of",n, "and", m,"is",n-m)
    
elif ch ==3:
    print("Multiplication of",n, "and", m,"is",n*m)
    
elif ch ==4:
    print("Division of",n, "and", m,"is",n/m)
    
elif ch ==5:
    print("Floor Division of",n, "and", m,"is",n//m)
    
elif ch ==6:
    print("Modulus of",n, "and", m,"is",n%m)
    
elif ch ==7:
    print("Exponential of",n, "and", m,"is",n**m)
    
else:
    print("Select a Valid Choice to perform the Operation")
    
'''



#  Harrys Thought Process and Solution 

a=50
b=3

print("The Value of", a, "+", 3, "is:", a+b)
print("The Value of", a, "-", 3, "is:", a-b)
print("The Value of", a, "/", 3, "is:", a/b)
print("The Value of", a, "*", 3, "is:", a*b)
print("The Value of", a, "//", 3, "is:", a//b)
print("The Value of", a, "**", 3, "is:", a**b)