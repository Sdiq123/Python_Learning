'''
Maanlo merey paas ek variable hein, aur mainey usey ek function ke andar banayi hein , to kya main usey function ke bahar use kar sakta hun ?
nahi karsakta , kyunki vo ek local variable hein

on the other hand maanlo mainey ek variable function ke bahar banaya hein, vo main function ke andar bhi use karsakta hun , as long as function ke andar us naam ka variable na ho - tab tak 

Local Variables Destroy hojatey hein jaisey heen aapka function return karta hein
Global Variables Destroy nahi hotey, vo programme main baney rehtey hein
'''

# x = 4 
# print("x is now a global variable",x)

# def hello():
#     x = 5
#     print(f"The local x is {x}")    # local variable function ke nadar heen define hota hein aur accessible bhi function ke andar heen hotey hein
#     print("I am inside the Function , where i am in Local")
    
# print(f"Now before calling local, global x is : {x}")
# hello()
# print(f"Now after calling local, global x is : {x}")


# hello() ke andar main aisa kya karun ki global variable bhi change hojaye 

# -------> example from the code base <---------

x = 10 # global variable

def my_function():
                # ab main kya karun is function ke andar taaki mera global variable change hojaye 
  global x      # 'global' keyword bolta hein ki global variable ko pakadlo aur uskey upar operation kardo
  x = 4
  y = 5 # local variable 
  print(y)

my_function()
print(x)
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function


