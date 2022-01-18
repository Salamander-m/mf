from math import *
x = float(input('input = '))

if x <= -4:
    y = -2
if x >= -4 and x <= 0:
    y = 0.25*x
if x >= 0 and x <= 2:
    y = x**2
if x >= 2:
    y = (-4*x+40)/8
print('Y =',y)