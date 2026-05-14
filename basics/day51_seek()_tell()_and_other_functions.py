'''
File Handling mein kuch miscellenious cheezein karney ke liye kya use karengey ye dekhtey hein chaliye

'''
# seek()
# maanlo ek file ke 6th character ko aap edit karna chahtey ho 
# f.read() karkey - usko edit karkey fir change karna chahtey ho , to nahi aisa ye bahut hectic process hein karney ka

with open('D:/Learnings/Python_Learning/basics/my_file.txt', 'r') as f:
  # Move to the 10th byte in the file
  f.seek(10)    # f.seek() kya kehta hein ki aap starting se read mat karo, ye 10th waley bite se karo

  # Read the next 5 bytes
  print(f.tell())  # tell() - tumharey file ka starting point ko bolta hein ki, taki pata chaley seek() - kahan se shuru ho raha hein karkey
  
  data = f.read(5)  # read() ka hamesha se ek argument hota hein ki vo kitna bytes tak read karega
  print(data)


'''
truncate() - Method

truncate()- Method se ham file ke size define karsaktey hein, 
'''

with open('D:/Learnings/Python_Learning/basics/sample.txt', 'w') as f:
  f.write('Hello World!')
  f.truncate(5)     # to issey ham file ke size ko restrict kar saktey hein

with open('D:/Learnings/Python_Learning/basics/sample.txt', 'r') as f:
  print(f.read())



