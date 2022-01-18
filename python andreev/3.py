from math import *
x = float(input('input = '))

if x >= -9 and x <= -5:
    y = -2 + sqrt(4 + (x+7)**2)
if x >= -5 and x <= -4:
    y = 2
if x >= -4 and x <= 0:
    y = x/-2
if x >= 0 and x <= pi:
    y = (-4*x**2)/pi**2+(4*x/(pi))
if x > pi and x <= 5:
    y = x-pi
print('Y = ',y)