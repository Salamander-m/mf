from math import *
x = float(input('input = '))

if x < -6:
    y = 2
if x >= -6 and x <= -2:
    y = (x+2)/4
if x >= -2 and x <= 0:
    y = 2 - sqrt(4 - (x+2)**2)
if x >= 0 and x <= 2:
    y = sqrt(4 - x**2)
if x >= 2 and x <= 3:
    y = -x + 2
print('Y =',y)