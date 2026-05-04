'''
        Break & Continue in Python
Loops Iteration by Iteration kaam kartey hein, ek Iteration pehley execute hogi, phir doosri excute hogi, phir teesri
Tum agar chahtey ho ki ek particular Iteration par tum loop ko exit kardo aur 
Ek Particular Iteration par Loop ko Skip Kardo (code ka jo body hein vo us iteration par skip kardein) agar aisa karna chahtey hein to continue use karsaktey hein
To is tarah ka kaam kartey hein Break aur Continue ke statements
'''

# for i in range(12):
#     print("5 X ", i+1 ,"=", 5*(i+1))
#     if (i == 9):
#         break    # break statement kahega is loop ko chodh kar nikaljao
    
print("Loop ko Chod kar nikalgaya")

'''
Continue main kya hoga - Iteration ko chod kar nikaljao
'''

for i in range(12):
    if (i == 9):
        print("Main ye iteration 1==9 chodh kar i==10 main jaa raha hun")
        continue #continue se upar jo bhi likha ho vo execute hoga 
    print("5 X ", i+1 ,"=", 5*(i+1))
    # if (i == 9):
    #     continue