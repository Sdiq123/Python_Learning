'''
Agar aap ki khud ki ek python application ho, aur particular action par aap throw kardo error to aap kis tarah karogey ?
Aap raise keyword ka istemaal karogey , custom errors throw karogey 

Error raise karney ka main reason kya hein aur kyun error ko raise karna hein , error raise karney ka main reason hein ki programme ruk jaye aur kuch dusra unexpected na hojaye 
'''
a = int(input("Enter any value between 5 and 9"))

if(a<5 or a>9){
    raise ValueError("Value should be between 5 and 9")
}

'''
Defining Custom Exceptions

Custom Exceptions ko  define karsaktey hein ek nayi class banakar
'''
# Quiz - rite now user can write only numbers , that is integers, but he cannot write strings 
# If the user writes quit, then user should not get any error 

# --------------------I Have Solved this Quiz------------------------------

a = (input("Enter any value between 5 and 9"))
if str(a) == 'quit':
    print(f"{a} is an str....")
else:
    if(int(a)<5 or int(a)>9):
        raise ValueError("Value should be between 5 and 9")
    
    
    
        
        