from math import *
x = float(input('input = '))

if x >= -4 and x <= -2:
    y = x + 3
if x >= -2 and x <= 4:
    y = -0.5*x
if x >= 4 and x <=6:
    y = -2
if x >= 6 and x <= 10:
    y = -2 + sqrt(4 - (x-8)**2)
print('Y = ',y)