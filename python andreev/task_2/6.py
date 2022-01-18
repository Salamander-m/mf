from math import *
x = float(input('input = '))

if x <= -5:
    y = -3
if x <= -3 and x >= -5:
    y = x + 2
if x >= -3 and x <= 3:
    y = sqrt(9-x**2)
if x >= 3 and x <= 8:
    y = (3*x-9)/5
if x >= 8:
    y = 3
print('Y = ',y)