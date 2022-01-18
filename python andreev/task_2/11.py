from math import *
x = float(input('input = '))

if x >= -3 and x <= -2:
    y = -(x+2)
if x >= -2 and x <= -1:
    y = sqrt(1-(x+1)**2)
if x >= -1 and x <= 1:
    y = 1
if x >= 1 and x <= 2:
    y = -2*x+3
if x >= 2:
    y = -1
print('Y =',y)