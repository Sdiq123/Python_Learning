import os

files = os.listdir("D:/Learnings/Python_Learning/basics/clutteredFolder")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename("D:/Learnings/Python_Learning/basics/clutteredFolder/{file}","D:/Learnings/Python_Learning/basics/clutteredFolder/{i}.png")
        i = i + 1