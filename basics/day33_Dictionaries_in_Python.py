'''
Aap log keys ke corresponding kuch values dekh saktey ho
word jo hum dhundtey hein vo hein KEY aur jo uska meaning hein usey boltey hein VALUE

Dictionary mein jo access hota hein vo bahut fast hota hein kyunki inki khud ki access karney ka index hota hein
'''

dic = {
    "Sadiq" : "Human Being",
    "Spoon" : "Object"
}

print(dic["Sadiq"])     # Basically Key Value pairs ka Combination 
                        # Aap isey use karsaktey ho ek particular class ke bachhon ke marks store karney ke liye
                        # Employee Id se Employee Name se map kar saktey ho 
                        # Basically Mapping ko easy banadeta hein
                        
dic1 = {
    344 : "Harry",
    56 : "Shubham",
    678: "Zakir",
    567: "Neha"
}                        
                        
print(dic1[567])                     
                   
# Dictionary are Ordered Collection of data items    
# Python 3.7 onwards Dictionaries Ordered Hein, Pehley Dictionaries UnOrdered hua karti thi   

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)

#--------------------------------> Accessing a Single Variable - 2 Types <-----------------------------------------------
# Type - 01
print(info["name"]) # If a Key doesnot exists then this type throws an error, saying that key is not there
# Type - 02
print(info.get("name")) # If a Key doesnot exists then it does not throw an error, it gives None in the output and programme is not stopped

#---------------------------------> Accessing Multiple Values / Accessing Keys / Accessing Values

print(info.keys()) #--- Accessess only the keys in a dictionary using items

#  Aap ek ek karkey inki saarey keys ko iterate karsaktey ho 

for key in info.keys():
    # print(info[key])
    print(f"The value corresponding to the key {key} is {info[key]}")
    
    
print(info.values()) #--- Accesses only the values in a dictionary using items


#----------------------------------> Accessing Key-value pairs
# Key Value Pairs ko Access karsaktey hein Item Index karkey

print("printing key value pairs...........")
print(info.items())     # to ye mujhey keyvalue pairs de deta hein

for key, value in info.items():
        print(f"The value corresponding to the key {key} is {value}")

# Dictionary ka use sirf mapping create karney ke liye