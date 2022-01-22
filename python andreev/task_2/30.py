from math import *
x = float(input('input = x '))
y = 0
R = int(input('input R = '))
if x <= -4:
    y = 2
if x >= -4 and x <= -2:
    y = -R - sqrt(R**2-(x+2)**2)
if x >= -2 and x <= 0:
    if x == -2:
        print('Y =',y)
    y = 0
if x >= 0 and x <= 3:
    if x == 1:
        y = x
    else:
        k = 3 / (R+1)
        y = -k*x
if x >= 3 and x <= 5:
    if x == 3:
        print('Y =',y)
    y = -1 + sqrt(R**2-(x-3)**2)
if x >= 5:  
    y = -1
print('Y =',y)