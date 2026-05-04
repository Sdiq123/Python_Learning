'''
While Loop

while ko usually complex conditions ke saath istemaal kartey hein
Jab tak Condition True Hogi while Loop Execute hota rahega 
Jab Condition False Hojayegi While Loop Ka Execution Band Hojayega , Interpreter Bahar Ajayega 

Doosri Programming Languages mein do-while Loop hota hein , jismey kam se kam ek baar to zarur execute karta hein loop ko irrespective condition true ho ya na ho 

kabhi Kabhi Question aata hein ki " Emmulate do - while Loop in Python "

'''

# for i in range(3):
#     print(i)
 
'''
Example -1
'''
    
# i = 0        # Initialization
# while(i<=3):  # Jab tak i ki value choti hein i ko print kartey raho 
#    print(i)  # Aur Iteration ke liye i ki condition mandatorily check hogi
#    i+=1
   
# print("Done with the Loop")

'''
Example-02
'''

# i =  int(input("Enter the number : "))       # Initialization
# while(i<=38):  # Jab tak i ki value choti hein i ko print kartey raho 
#    i = int(input("Enter the number: "))  # Aur Iteration ke liye i ki condition mandatorily check hogi
#    print(i)
   
# print("Done with the Loop")

'''
Example-03 -> Decrementing Loop
'''
count = 5
while(count >0):
    print(count)
    count = count - 1  #while Loop mein agar condition ki galti kardi to infinite Loop ke andar print karta chala jayega 
                       #Suppose count = count+1 kardo to ye infinite loop mein chalna shuru hojayega
else:                       #While Loop ke saath aap else ka bhi istemaal karsaktey hein , agar while loop ke andar nahi gaya to else ke andar chala jayega     
    print("I am inside else") # jab Bhi Condition False Hjayega to Else wala execute kardega 
    
    
'''
do {
    # loop body
} while(condition);

--> The Most common Technique to emulate a do-while loop in Pythin is to use a
infinite while loop with a break statement wrapped in an is statement that checks a given condition and breaks the iteration if the condition becomes true
'''

#  Example - 01

# while True:
#     number = int(input("Enter a positive number: "))
#     print(number)
#     if not number > 0:
#         break
    
    
'''
Explanation 
This loop uses True as its formal condition. This trick turns the loop into an infinite loop.
Before the conditional statement, the loop runs all the required processing and updaates the breaking condition.
If this condition evaluates to true, then the break statement breaks out of the loop, and the program execution continues its normal path  
'''

# Example - 02

i = 0
while True:
    print(i)
    i = i + 1
    if(i%100 == 0):
        break