'''
            Functions in Python
Maanlo agar aap apney code ko, code ke logic ko Multiple times use karna chahtey ho
FUnctions ka sirf yahi kaam hota hein ki Logic ko separate kardo main function se aur uskey baad iskoo refer kardo jo kaam karna hein vo ye kaam kardega 
code mein unnecessary code ki lines nahi badengi aur logic ko sirf ek heen baar implement karney se ye shi hojata hein

Function sirf code likhney ka ek tariqa hein 
Maanlo aap ek block of code ko apney programme mein das ya pachaas baar use kar rahey ho 
To aap kya usey baar baar istemaal karogey (assuming that particular block of code is 50-100 lines of code)
to aap usey ek function mein wrap kardengey jissey aap usko baar baar sirf call karney se istemaal karsaktey ho 

Functions do tarah ke hotey hein 
1. Built in Functions - hamey def keyword ke madad sey define karney ki zarurat nahi hoti
2. User-defined functions - jo user khud bana raha hein , jo def keyword ki madad se banti hein

1.Built - in Functions
        Ex : min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print() etc....


'''
a=9
b=8
gmean = (a*b)/(a+b)
print(gmean)

c=8
d=3
gmean1 = (c*d)/(c+d)
print(gmean1)

def calculateGmean(a,b):    # def ke baad jo mainey likha hein vo function ka naam hein-a aur b Arguments hein jo Function accept kar raha hein
    mean = (a*b)/(a+b)
    print(mean)
    
def isGreater(a,b):
    if(a>b):
        print("First Number : ",a ,"is Greater")
    else:
        print("Second Number: ",b,"is Greater or equal")

def isLesser(a,b):
    pass                # pass ka matlab ye hein ki main wapas aunga aur phir se function likhunga
                        # pass ka matlab aagey nikal jao aur apna process shuru karo
                        # pass likhney se error nahi dega

e = 7
f = 8
calculateGmean(e,f)
isGreater(e,f)
isLesser(e,f)






