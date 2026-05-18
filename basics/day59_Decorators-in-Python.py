'''
Decorators vo Functions hotey hein jo ki dusrey Functions ko change karkey return karkey hein
@ ye syntax python main kaisey kaam karta hein dekhengey
aur decorate karney wala function hamesha upar likhtey hein , aur jo le raha function usey hamesha neechey likhtey hein
'''



# Decorator ek Function ko Modify kardeta hein
def greet(fx):   # ye ek function ko as a Input lega, to agar main greet ko hello() ke upar lagaunga , to hello() ko as a input lega , aur aagey aur nichey ye laga dega, kyunki input function ko beech mein call kar rahey hein
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks for using this function")
    return mfx


# Main Chahta hun ki ye function pehley Good Morning karey aur uskey baad kuch karkey de
@greet
def hello():
    print("Hello World")
    

# Main isko Aisey bhi likh sakta hun
greet(hello)()     # to ye karney ka sabsey bahut aasaan tarika hein



@greet
def add(a, b):
    print(a + b)

add(1,2)
# This particular function will throw an error, as it is taking a decorator and the decorator is not handled to take arguments , hence in the decorator you have to always add *args and *kwargs kyunki 'mfx' arguments nahi lega
# Agar main Function mein koi bhi 'Arguments' hein to main 'mfx' mein likhunga *args and **kwargs 
