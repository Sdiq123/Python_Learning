'''
Function Caching Tab Upayog kiya jaata hein, ya phir tab use kartey hein , Jab EK heen Function , EK heen Value ke liye kai baar run hota hein

Aisey mein ham "Memoization Technique" ka istemaal kartey hein

Assume ki merey paas ek computationally bahut heen expensive Function hein, maalo 10seconds le raha hein ek-ek baar run karney ke liye

Aapko Code Likhney ki Zarurat nahi hein,  "functool"  karkey ek module hein python mein, jo ki ye cheez automatically karta hein
'''

import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5
    
# lru_cache se kya hojayega ye Function Memoize Hojayega    
# Memoize - to store the result of a computation so that it can be subsequently retrieved without repeating the computation

# Ye Cache maintain karta hein har ek Programme ke Run Mein , Agar main phir se Programme chalaun to Cache phir se khaali hojayegi aur phir start hogi 

# kab use karna hein jab mujhey pata hein ki kuch Limited Values ke Liye heen Mera Function Run ho raha hein, aur main vhahta hun ki mera user jo hein jaldi se fetch kar paye function ke result ko
# Databases ke results ko retrieve karna bhi usually cache hota hein     


# lru_cache , idhar memory mein values store ho rahi hein aapkey programme ke run honey ke dauran , Koi separate file nahi ban rahi hein, ya database mein jaakar store nahi ho rahi hein     
    
print(fx(20))    
print("done for 20")    
print(fx(2))    
print("done for 2")    
print(fx(6))    
print("done for 6")    



print(fx(20))    
print("done for 20")    
print(fx(2))    
print("done for 2")    
print(fx(6))    
print("done for 6")    
    