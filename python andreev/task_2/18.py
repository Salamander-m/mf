from math import *
x = float(input('input = '))

if x <= -2:
    y = -x-2
if x >= -2 and x <= 0:
    y = sqrt(1 - (x+1)**2)
if x >= 0 and x <= 4:
    y = -sqrt(4 - (x-2)**2)
if x >= 4:
    y = -0.5*x+2
if x >= 6:
    y = -1
print('Y =',y)