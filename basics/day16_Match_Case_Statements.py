'''
Agar Aap ek Modern Python Developer hein to main sabsey pehley aap se Match Case Statement Puchunga
Ye Python Main Naya Addition Hua Hain jo ki 3.10 ke baad hua hein
Match Case Statements Python Programming ko Bahut zyada Mazbut banatey hein 

Aap Ke Paas Ek Variable hain aur aap us variable ki aap Matching Kar rahey ho basically 
varibale ki value 17 hein , 18 hein , 19 hein Maanlo tab kya karna hein ?

Three Main Cheezein Hein Match Case Statements ki 

1. The Match Keyword 
2. One or More Case Clauses
3. Expression for each case

Agar aap C , C++ Se aarahey ho to aap ko pata hoga ki agar switch case statement use kar rahey ho aur koi case match kargaya to break use karna aniwarya hojata hein, kyunki agar case2 match hogaya , to case3 aur case4 bhi chaljayega condition na match honey ke bawajood
magar python mein yahan break use karney ki zarurat nahi , jo bhi case match hoga wo heen run hoga 

A Match statement will compare a given variables value to different shapes, also referred to as the pattern. The Main Idea is to keep on comparing the variablewith all the present patterns until it fits into one





'''

x = 4 
#  x is the variable to match
match x: 
    # if x is 0:          Matlab Case ke baad jo bhi number hoga vo x ka heen value hoga jo alag alag hosakta hein 
    case 0:
        print(" x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    
    # Empty case with if-condition
    case _ if x < 10: # Default Case ke liye Hamesha Underscore Use hota hain 
        print("x is < 10")
    
    # Default Case will be Matched only if the above cases were not matched 
    
    
a = int(input("Enter the value of 'a' you want to match: "))

match a:
    case 0:
        print("x is zero")
        
    case 4:
        print("case is 4")
        
    case _ if a!= 90:
        print( a, "is not 90")
    case _ if a!= 80:
        print( a, "is not 80")
   
    case _ :
        print( a)