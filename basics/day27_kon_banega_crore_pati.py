# Create a Programme capable of displaying questions to the user like KBC.
# Use List Data Type to store the questions and their correct answers 
# Display the Final Amount the person is taking home after playing the game.

print("------Welcome to Kon Banega Crorepati........")

list_of_questions = [
    "1. What is the Capital of India",
    "2. What is the National Fruit of India",
    "3. What is the National Bird of India"
    
]

tuple_of_options_for_1 = ("1) Lucknow","2) Chandigarh", "3) Bhopal", "4) Delhi",)
tuple_of_options_for_2 =("1) Watermelon","2) Banana","3) Orange","4) Mango",)
tuple_of_options_for_3 =("1) Pegion","2) Parrot","3) Peacock","4) Koyal",)

user_input = input(print("Enter 'yes' to proceed with playing KBC or Enter 'no' to Terminate the programme"))
if user_input == 'yes':
    print(list_of_questions[0])
    print("options for the above question:",tuple_of_options_for_1[:])
    answer = int(input("Enter the Option: "))
    if answer == 4:
        money = 100
        print("Yes you won",money)
    else:
        print("wrong answer choosen and no money is won by you")
        exit
    print(list_of_questions[1])
    print("options for the above question:",tuple_of_options_for_2[:])
    answer = int(input("Enter the Option: "))
    
    
    
# My solution is this much itself, money you can add in each if , else statements , but this logic wont be valid for a wrong scenario, were suppose first answer is wrong
# Then it should exit the loop, which it wont exit 
# iska solution day 39 ke python fille main hein dekhlena....


    