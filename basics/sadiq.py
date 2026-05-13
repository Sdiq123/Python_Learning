def welcome():
    print("Hey you are welcome from sadiq")
    

print(__name__)

# welcome() function importing ke time par execute na ho isiliye ye check lagaya jaata hein
if __name__ == "__main__":    
    welcome()


'''
Agar ye cheez if __name__=="__main__"  ->  ye cheez agar file mein hein to 
iska matlab ye hein ki welcome() Funtion ko main yahi se call karunga 

kyunki agar name variable main nahi hein to main welcome() Function ko yahan (is wali file) se run karunga warna , jahan import ho raha hein wahan run karunga 
basically __name__ variable ke value ke upar jayega

kyunki agar name variable main nahi hein to main welcome() Function ko yahan (is wali file) se run karunga warna , jahan import ho raha hein wahan run karunga 
basically __name__ variable ke value ke upar jayega

dono files ek baar chala kar dekhlo day45 aur sadiq.py , name 

'''
