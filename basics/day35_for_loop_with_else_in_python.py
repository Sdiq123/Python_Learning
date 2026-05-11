'''
else - is not necessary to be used with only if statement, It can also be used with for loop
agar for loop ke andar control nahi jayega, to else wala block chalega 

you can also use else block in the while loop

Agar aap else use kar rahey ho for loop mein , to hamesha else for loop ke successfully khatam honey ke baad heen chalega

'''

# for i in []:
#     print(i)
# else:
#     print("Sorry no i")

# for i in range(6):
#     print(i)
#     if i == 4:
#         break
# else:                       # else ka matlab hein loop successfully khatam hua hein, break nahi hua hein
#     print("Sorry no i")     # yahan par obviously else wali block print nahi hogi 
 
# same cheez agar main while loop mein bhi use karsakta hun 
    
i = 0 
while i < 7:
    print(i)
    i = i + 1
    # if i == 4:        # agar main yahan par break nahi use karunga to else wala block print hojayega
    #     break
else:
    print("Sorry no i")
   
    
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")
print ("Out of loop") 
