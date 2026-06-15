import math
import time
from turtle import *
def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)-5*math.cos(2*k)-2*math.cos(3*k)-math.cos(4*k)

speed(0)
bgcolor("black")

myDict1 = {} # +, + 
myDict2 = {} # +, - 
myDict3 = {} # -, - 
myDict4 = {} # -, + 

for i in range(500):
    if hearta(i)>0 and heartb(i)>3.8:
        myDict1[hearta(i)] = heartb(i)
        
    elif hearta(i)>0 and heartb(i)<0:
        myDict2[hearta(i)] = heartb(i)
        
    elif hearta(i)<0 and heartb(i)>3.8:
        myDict4[hearta(i)] = heartb(i)
        
    elif hearta(i)<0 and heartb(i)<0:
        myDict3[hearta(i)] = heartb(i)
        

myKeys1 = list(myDict1.keys())
myKeys2 = list(myDict2.keys())
myKeys3 = list(myDict3.keys())
myKeys4 = list(myDict4.keys())
myKeys1.sort()
myKeys2.sort()
myKeys3.sort()
myKeys4.sort()
myKeys2.reverse()
myKeys3.reverse()

myDict = myDict1|myDict2|myDict3|myDict4
myKeys = myKeys1+myKeys2+myKeys3+myKeys4

for i in range(500):
    goto(myKeys[i]*10, myDict[myKeys[i]]*10)
    print(myDict[myKeys[i]])
    color("#ffffff")
