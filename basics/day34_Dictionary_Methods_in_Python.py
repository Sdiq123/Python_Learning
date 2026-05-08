'''
Dictionary Methods 
'''
ep1 = {122: 45, 123: 89, 567: 69, 670: 69}  # hamney bahut saarey persons ke variable ko store kardiya hein ek variableke andar

ep2 = {222: 67, 568: 90}
ep3 = {222: 67, 568: 90, 756:67}


ep1.update(ep2)         # updating one dictionary into another
print(ep1)

# ep3.clear()
# print(ep3)          # ep3 khaali hojayegi aur ek empty dictionary print kardegi

# Empty dictionary kaisey banatey hein empt = {} , to empt ek empty dictionary banjayegi

# pop()  Method Key Value pair ko remove karney ke liye use kartey hein
ep1.pop(122)
print(ep1)

# popitem() ye last item (key-value pair) ko remove kardeta hein dictionary se  
ep1.popitem()
print(ep1)

# del - keyword ye delete kardeta hein puri dictionary ko 
# del ep1    # if you want to give a particular key in the dictionary , then do give it otherwise it will delete the entire dictionary itself

del ep1[122]        # ye wali entry hat jayegi meri dictionary se 





