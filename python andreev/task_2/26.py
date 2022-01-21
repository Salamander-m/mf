from math import *
x = float(input('input = '))
y = 0

if x <=-6:
    y = -2*x-14
if x >= -6 and x <= -2:
    y = -2+sqrt(4-(x+4)**2)
if x > -2 and x <= 2:
    y = log((2+x),2)
if x >= 2 and x <= 4:
    if x == 2:
        print('Y =',y)
    y = sqrt(1-(x-3)**2)
if x >= 4:
    y = 0
print('Y =',y)