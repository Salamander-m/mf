from math import *
x = float(input('input = '))

if x <= -3:
    y = -(x+3)
if x >= -3 and x <= 0:
    y = sqrt(9-x**2)
if x >= 0 and x <=6:
    y = -0.5*x+3
if x >= 6:
    y = (x-6)
print('Y =',y)