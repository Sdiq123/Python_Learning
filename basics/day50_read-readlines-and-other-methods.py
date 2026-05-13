'''
readline() - sequence of lines ko read karega
'''

# f = open('D:/Learnings/Python_Learning/basics/my_file.txt', 'r')
# i = 0

# while True:
#         i = i + 1
#         line = f.readline()
#         m1 = int(line.split(",")[0])
#         m2 = int(line.split(",")[1])
#         m3 = int(line.split(",")[2])
#         print(f"Marks of student {i} in maths is: {m1}")
#         print(f"Marks of student {i} in maths is: {m2}")
#         print(f"Marks of student {i} in maths is: {m3}")
#         if not line:
#             break
#         print(line)
        
'''
writeline() - sequence of lines ko write karega 

writeline() - sequence main nahi dalega, wo hamey heen handle karna padta hein

'''        

f = open('myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()

