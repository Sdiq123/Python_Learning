* walrus operator has newly been introduced in python 
* Usually assigning a value and using it are two separate steps, The Walrus Operator Combines *these two steps into one 
* walrus operator is this := 

* without walrus operator
numbers = [1,2,3,4,5]
n = len(numbers)
if n>3:
    print(f"List is too long :{n}")

* with walrus operator
numbers = [1,2,3,4,5]
if (n:= len(numbers)) > 3 :
        print(f"List is too long :{n}")
