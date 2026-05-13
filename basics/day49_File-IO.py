'''
File Handling in Python 

Ek file ko open kaisey kiya jata hein, append kaisey kiya jata hein us text file mein

Files text files bhi hosakti hein aur binary files bhi hosakti hein 
'''

# open() = File ko openkarney ke liye use karsaktey ho
#          Two Arguments, first is the file name and the second is the Mode in which you are working on the file 
#          Mode r - reading , w - writing and a - append , karsaktey hein vo file mein
#          r - mode is a default mode

# READING A FILE
# f = open('D:/Learnings/Python_Learning/basics/my_file.txt', 'r')
# # print(f)
# text = f.read()
# print(text)
# f.close()

'''
# Agar write mode mein aisy file kholdun jo ki exist heen nahi karti ho , to vo us file ko nayi banadega

# mode - rt => read text , jo ki by default hota hein , laganey ki zarurat bhi nahi hein
# mode - rb => read binary , jo content hein file mein vo binary ke form aayega

'''

# WRITING A FILE

f = open('D:/Learnings/Python_Learning/basics/my_file.txt', 'a')
f.write('Hello, world!')
# f.close()

# agar same file ko main 'a' - append mode mein kholunga,to jitni baar main file kholunga to utni baar append hoga

# with statement ka use karkey file ko close karney ki zarurat nahi hein

with open('my_file.txt', 'a'):
    f.write("Hey I am inside with........")

# file handling kyun zaruri hein , agar aap koi game bana rahey ho to to usmey koi cheezein store karna chahtey ho to aap isko use karsaktey ho 
# ek - jugaadu database ki tarah use karsaktey ho