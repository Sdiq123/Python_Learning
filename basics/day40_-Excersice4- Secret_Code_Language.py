'''
How to make a secret code language

# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
if the word contains atleast 3 characters, remove the first letter and append it at the end
now append three random characters at the starting and the end
else:
simply reverse the string

## Decoding:
if the word contains less than 3 characters, reverse it
else:
remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

### Your program should ask whether you want to code or decode
## [Next Lesson>>](https://replit.com/@codewithharry/41-Day41-Short-Hand-if-else)


'''



# do this excersise when you are revising ......
# [1:] --> this is a slicing operation, which escapes from the first step 
#-----------------------------------------------------------------------------------------
#----------------------------My Solution-----------------------------
#------------------------------------------------------------------------
word = list(input("Enter a word you want to decode : "))

if len(word) > 3:
    first_word = word[0]
    removed_first_word = word[1:]
    print(removed_first_word)
    w1 = removed_first_word.append(first_word)
    print(w1)
    # w1.insert(0,789)
    # w1.append(321)
    
    
    
    
