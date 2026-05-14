'''
------------Reduce-------------
ye bhi higher order function hein 
ye bhi function as a argument leta hein
par ye hame import karna padta hein
'''


from functools import reduce

# List of numbers
numbers = [1, 2, 3, 4, 5]
# numbers = [3, 3, 4, 5]
# numbers = [6, 4, 5]
# numbers = [10, 5]
# numbers = [15]
# Aisa heen kaam karta hein ye



# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)

# Print the sum
print(sum)