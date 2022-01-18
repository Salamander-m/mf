from math import *
x = float(input('input = '))

if x <= -3:
    y = 1
if x >= -3 and x <= -1:
    if x == -3:
        print('Y =',y)
    y = -sqrt(4-(x+1)**2)
if x >= -1 and x <= 2:
    y = -2
if x >= 2:
    y = x - 4
print('Y =',y)