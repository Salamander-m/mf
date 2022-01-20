from math import *
x = float(input('input = '))
y = 0

def ch(x):
    ans = 1/2*(e**(x)+e**(-x))
    return(-ans)
    

if x <=-5:
    y = 2
if x >= -5 and x <= -1:
    y = 2 - sqrt(4-(x+3)**2)
if x >= -1 and x <= 1:
    if x == -1:
        print('Y =',y)
    y = ch(x)
if x >= 1 and x <= 2:
    if x == 1:
        print('Y =',y)
    y = 0
if x >= 2 and x <= 4:
    y = sqrt(1 - (x-3)**2)
if x >= 4:
    y = 0
print('Y =',y)