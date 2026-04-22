# Comments, Escape Sequences and Print Statements 
'''
\n  -> Ye ek new line ka escape sequence character hein 
    -> apkey print statement ko ek new line main lekey jaata hein 
    -> Ye kya tha \n ye ek escape sequence character hein 
    -> Ye dikney mein to do characters hein par internally ye ek heen character hein 

\"  -> ye double quotes ka escape sequence character hain 
'''
# PRINT
print("Sadiq is a good boy \nand Rohit also is a good boy")

# Print main aap ek character nahi balki bahut saarey charcters daal saktey ho
print ("Hey", 6, 7)

# Aap Kabhi bhi teen cheezon ko join karna chahtey ho teen cheezon sey aap separator ka use karsaktey ho 
print("Hey", 6, 7, sep="~") # Default Seprator hamesha Space hota hain 

# end='end': Specify what to print at the end. Default is '\n' 
# print Statement ke end main isko kya print karna hein, vo end bolta hein 
print("Hey", 6, 7, sep="~", end="009") # Jo Bhi Agla Print statement hoga ussey pehley ye end wala laga dega
print("sadiq")                         

# end with \n 
print("Hey", 6, 7, sep="~", end="009\n") # Jo Bhi Agla Print statement hoga ussey pehley ye end wala laga dega
print("sadiq")




# -----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Agar koi bhi line of code ko upar ya nichey lekey jaana hein to 'Alt' dabakey 'downward ya upward' Arrow Aram se use kar saktey hein upar nichey karney ke liye 
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------

# ESCAPE SEQUENCE CHARACTERS 
'''
To Insert a Character that cannot be directly used in a string we can use an escape sequence character 

An Escape Sequence Character is a backslash \ followed by the character you want to insert 
'''

print (" Hey I am a Good Boy, How are you - are you a \"Good Boy\"")

print (' Hey I am a Good \'Boy\', How are you - are you a "Good Boy"')