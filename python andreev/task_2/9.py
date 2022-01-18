from math import *
x = float(input('input = '))

if x >= -7 and x <= -3:
    y = x + 7
if x == -2:
    y = 4
if x >= -2 and x <= 2:
    y = x**2
if x >= 2 and x < 4:
    y = -2*x+8
if x >= 4:
    y = 0
print('Y =', y)