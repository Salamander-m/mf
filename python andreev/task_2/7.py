from math import *
x = float(input('input = '))

if x <= -3:
    y = 3
if x >= -3 and x <= 3:
    y = -3 + sqrt(9 - (x)**2)
if x >= 3 and x <=6:
    y = (-6*x+27)/3
if x >= 6:
    y = x - 9

print('Y = ',y)