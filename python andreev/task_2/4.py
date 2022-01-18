from math import *
x = float(input('input = '))

if x <= 0:
    y = -0.5*x-3
if x >= 0 and x <= 3:
    y = -sqrt(9-x**2)
if x >= 3 and x <= 6:
    y = sqrt(9-(x-6)**2)
print('Y = ',y)