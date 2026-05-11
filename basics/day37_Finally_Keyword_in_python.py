'''
try - except ke saath aap log finally bhi use karsaktey ho, for cleanups ke liye
finally ke andar daala hua code hamesha execute hota hein irrespective of whether error aaya ya nahi aaya
kabhi kabhi ham chahtey hein ki irrespective whether code creah ho ya na ho , kuch code hamesha execute ho 
'''


# try:
#     l = [1,5,6,7]
#     i = int(input("Enter the index: "))
#     print(l[i])
# except:
#     print("Some error occurred...")
    
# finally:                                
#     print("I am always executed")
    
# EK Main Doubt, instead of writin the finally keyword, main directly print likh sakta hun na to bhi ye kaam karega     
# Main Difference kahan aata hein aapko pata hein, jab aap same cheez ko ek function mein wrap kartey ho, tab ye main difference pata chalta hein
# Suppose main same code ko ek functin mein wrap kar raha hun named func1 

print("running the code inside the function..........")
 
def func1():
    try:
        l = [1,5,6,7]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1        # return 1 matlab pass hogaya , since try block execute hua, to ye function hamesha 1 heen return karega 
    except:
        print("Some error occurred...")
        return 0        # aur return 0 matlab error agaya
    finally:                                
        print("I am always executed")


# Finally ka matlab execute to karna heen hein chahey function execute hojaye, par isko to return karna heen hein 
# Finaaly ka sirf ye matlab nahi hein ki error aya to bhi return karega 
# Finally ka sabsey bada matlab ye hein ki , irrespective whether aap try waley mein return kar rahey ho ya except mein return karogey , vo cheez hamesha execute hogi


x = func1()
print(x) 
 
 
    
    