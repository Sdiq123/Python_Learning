'''
kabhi kabhi hamlog jab for loop lagatey hein to ham logon ko index ki zarurat padti hein
maanlo main ek list iterate kar raha hun aur mujhey vahan ek variable chahiye jo ki konsa element hein mujhey vo vo batadey, list ki konsi index chal rahi hein vo bata dey ,ek temporaray variable banakar usey karsaktey hein 
par aaj ham usey enumerate ke madad se banayengey , jo ki is task ko bahut easy kardega

enumerate function ko aap strings par bhi use karsaktey ho 
aur ye hamesha tuple mein return karta hein cheezon ko

'''
marks = [12, 56, 32, 98, 12, 45, 1, 4]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Sadiq, Awesome!!!!!")
#     index += 1


'''
Enumerate - har value ke saath saath uska index bhi dega 
'''
for index, mark in enumerate(marks):
    print(mark)
    if (index == 3):
        print("Sadiq , Awesome ...........")
        
        
fruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits):
    print(f'{index}: {fruit}')
    
'''
Unique use case - By Defualt index 0 se start hoti hein , but you can specify a different starting index by passing it as an argument to the enumerate function
'''
ruits = ['apple', 'banana', 'mango']
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


