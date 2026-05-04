''' Modules and Pip 
* Reusing the Code which has already been written by the other person 
* 2 Types Of Modules 
    (i) Built In Modules 
        Ye Modules Python Language ke saath heen Ship Hotey hein, Inhey aap ko externally install karney ki zaruarat nahi hein 
    
    (ii) External Modules 
        This is the code which other people have written 
        and this can be installed by pip 
        Ex - hamarey paas ek phone hein, hamey pata nahi ki ye phone kaisey kaam kar raha hein iski andar ki functonalities nahi pata 
             par phir bhi main isey use kar paa raha hun, ye ek Eternal Module hein 

Ex - pip install pandas 
-> jab main ye above command likhta hun tab 

-> Ek achhi si analogy se samjtey hein , jab bhi ham chotey they to jo bhi cheez mummy hamey bolti thi vo ham lakey ghar pe rakh detey they 

-> pip is Package Manager - jo bhi Module chahiye vo internet se install karkye hamarey python interpreter mein lakey rakhdetey hein 

jab terminal par ham python likkar python ke andar jatey hein , usey boltey hein REPL, which is
Read , Evaluate , Print , Loop 

'''

import pandas  # External Module 

import hashlib # Built In Module



'''
# Day 3 - Modules and pip in Python!

Module is like a code library which can be used to borrow code written by somebody else in our python program. There are two types of modules in python:
1. Built in Modules - These modules are ready to import and use and ships with the python interpreter. there is no need to install such modules explicitly.
2. External Modules - These modules are imported from a third party file or can be installed using a package manager like pip or conda. Since this code is written by someone else, we can install different versions of a same module with time.

## The pip command

It can be used as a package manager [pip](https://pip.pypa.io/en/stable/) to install a python module.
Lets install a module called pandas using the following command

```bash
pip install pandas
```

## Using a module in Python (Usage)
We use the import syntax to import a module in Python. Here is an example code:

```python
import pandas

# Read and work with a file named 'words.csv'
df = pandas.read_csv('words.csv')
print(df) # This will display first few rows from the words.csv file
 
```

Similarly we can install other modules and look into their documentations for usage instructions.\
We will find ourselved doing this often in the later part of this course

## [Next Lesson>>](https://replit.com/@codewithharry/04-Day4-Our-First-Program)





'''