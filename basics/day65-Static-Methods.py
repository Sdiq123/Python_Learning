'''
Static Methods vo Methods hotey hein jo na hi Instance ko belong kartey hein aur na heen class ko

Static Methods ka Istemaal Tab kiya jaata hein , jab hamey class ke Instance ki zarurat heen na padey

'''

'''
Interview Question --> ask Rohit

Static Methods - Kya aapko ek class ke andar Method Bananey ke liye self use karna zaruri hota hein ?
Anser - No , Static Methods ke liye zaruri nahi hein 

'''



class Math:
    def __init__(self, num):
        self.num = num

    def addtonum(self, n):      # 'self' se ham us object ko refer kartey hein jispar hamney ye method chalaya hein
        self.num = self.num + n

    '''
    Maanlo ki isi 'Math' Class ke andar main utility Method Add Karna Chahta hun
    Kyun add karna chahunga main koi utility method ko ?
    kyunki kabhi kabhi mujhey merey class ke within ,ya phir jo main class ka object jo bana raha hun usmey do numbers ko add karney ki zarurat padsakti hein
    --->add to waisey bhi a+b se hojayega phir ?
    consider add as some complex calculation ex - Arithmetic Mean , Us tarah ke calculation ka aisa Method banana hein, to main ek static method bana sakta hun
    Static Method ka ek sabsey achha faida hota hein ki, zaruri nahi hein ki aap ek instance ko call karo , aap directly method ke arguments se call karsaktey ho, ye ek normal method hein par rehta class ke andar hein
    ---> Agar ye normal method hein to aap isey class ke andar kyun daal rahey ho bahar nikaal lo na easy hoga ?

    Main ye wali Method ko Class ke andar isiliye daal raha hun taki , Agar koi bhi ye 'Math' wali Class import karey to ye uska laabh uta sakey
    'Static Method' ko Class ke saath ship karna chahta hun

    Ham isey class ka hissa bana rahey hein without using 'self' , aapko self keyord istemaal karney ki zarurat nahi hein


    '''

    @staticmethod   # aap isey independently bhi call karsaktey ho , ye class Independent method hein 'Ex - print(Math.add(5+7))' 
    def add(a, b):
        return a + b
    
'''
Class ka naam istemaal karkey bhi call karsakta hun , aur instance ka naam istemaal karkey bhi call karsakta hun
'''
    
# result = Math.add(1,2)
# print(result)

a = Math(5)
print(a.num)

a.addtonum(6)
print(a.num)

b = Math(6)
print(b.add(3,4))