'''
OS Module - aapkey Operating System ke bahut saarey operations ko execute karney mein madad karta hein, jaisey aap 

This is a Built In Module in Python

Bulk Actions karsaktey ho , file ko read karney ke terms mein, folder ko create karney ke terms mein 
'''

# import os

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0,100):
#     os.mkdir(f"data/Day{i+1}")



'''
To Rename a file, use this - rename(source, destination) Function to be used
'''

# import os 

# for i in range(0, 100):
#     os.rename(f"data/Day{i+1}",f"data/Tutorial{i+1}")


'''
TO list the folders inside a a folder, use this method listdir()
'''
import os
folders = os.listdir("data")

print(folders)