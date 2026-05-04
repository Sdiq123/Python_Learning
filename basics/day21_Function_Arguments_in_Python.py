'''
Function is used to separate the code
Lekin Bahut saarey aisey tarkey hein jisey ki Function ko Argument pass karsaktey hein
As a Tuple Pass karsaktey hein aur as a dictionary bhi pass karsaktey hein 
bahut saarwy Arguments jo aap bulk mein paas karna chahtey ho vo kaisey pass kartey hein chaliye samajtey hein

There are 4 Types of Arguments which we can provide in a function

1. Default Arguments
2. Keyword Arguments
3. Variable Length Arguments
4. Required Arguments

'''


'''
Example of Required Arguments - ye Arguments to aap ko deney heen deney hein 
'''

def average(a,b):
    print("The average is ",(a+b)/2)
    
average(4,6)

# def name(fname, mname, lname):
#     print("Hello,", fname, mname, lname)

# name("Peter", "Quill")




'''
Example of Default Arguments
'''
def average(a=9,b=1):
    print("The average is ",(a+b)/2)

# Examples of Calling Default Arguments in the Functions 
     
average()       # yahan par aapko average ko arguments ke madad se call karney ki zarurat nahi hein
average(1,3)    # Yahan bhaley heen default values ho, kyunki explicitly function call mein variables pass ho rahey hein to yahi sey call karega
average(1)      # Yahan a ki value 1 lega aur b ki value default lelega
average(b=10)

def name(fname, mname ="John", lname="Whatson"):
    print("Hello,",fname, mname,lname)
    
name("Amy","Agarwal","jain")


'''
        Keyword Arguments

ye simple arguments hein jinka aap order change kar saktey ho arguments ka

We can provide arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence, the the order in which the arguments are passed does not matter.
'''

average(b=9,a=21) # yahan arguments ko order main deney ki zarurat nahi hein


def name(fname, mname, lname):
    print("Hello,", fname, mname, lname)

name(mname = "Peter", lname = "Wesker", fname = "Jade")



'''
variable Legth Argument 
ye yahan kya karega aap basically numbers naam ke variable se pehley * (All) Laga rahey ho , jitney bhi variables se aap isko initialize kar saktey ho 
Aur * ke baad jo bhi varaiable aap usey detey ho vo isey as a tuple leta hein 
It is like a wildcard character , jitney bhi chahaey utney arguments variable main paas karsaktey ho 

Sometimes we may need to pass more arguments than those defined in the actual function. This can be done using variable-length arguments.

There are two ways to achieve this:

1. Arbitrary Arguments
While creating a function, pass a * 
before the parameter name while defining 
the function. The function accesses 
the arguments by processing them in the 
form of tuple.

2. Keyword Arbitrary Arguments
While creating a function, pass a * 
before the parameter name while defining 
the function. The function accesses the 
arguments by processing them in the form 
of dictionary.

'''

def avg(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
         sum = sum + i
    print("Average is:",sum/len(numbers))

avg(8.6,5,50,63,89,45)

# 1. Arbitrary Arguments
def names(*name):
    print(type(name))
    print("Hello,",name[0],name[1],name[2])

names("james","Buchanan","Barnes")

# 2. Keyword Arbitrary Arguments
def name(**name): # since dictionary is a key value you are trying to access it with keys
    print(type(name))
    print("Hello,",name["fname"], name["mname"],name["lname"])
    
name(mname = "Buchanan",lname ="Barnes",fname ="james" )

# ===============================================
# --------------------Return---------------------
# ===============================================
'''
Instead of printing aap value ko return kardo

return statement is used to return the value to the calling function
'''


def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)

c = average(5,6,7,8,9)
print(c)