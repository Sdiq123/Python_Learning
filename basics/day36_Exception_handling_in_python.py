'''
Programme ke code main aksar error aa heen jaat hein
kabhi kabhi mistake ek server ke dwara bhi hosakti hein
aapney suppose kuch records server se mangwaye aur vo records server se aana paye, aisey mein hamara python programme kabhi nahi ruk sakta hein
Isilye Python mein use kartey hein error handling, aur error handling ke liye python mein use kartey hein try-except waley block ko

'''

# a = int(input("Input Enter a number : "))  # suppose main yahan a ki jagah par harry likhdun, to obviously error ayega 

# print(f"Multiplication table of {a}")

# for i in range (1, 11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
    
    
try:
    num = int(input("Enter an integer: "))
    a = [6, 3]
    print(a[num])
except ValueError:
    print("Number entered is not an integer.")
except IndexError:
    print("Index Error...")