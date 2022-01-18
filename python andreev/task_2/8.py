from math import *
x = float(input('input = '))

if x <= -6:
    y = -2 + sqrt(4 - (x+8)**2)
if x >= -6 and x <= 2:
    y = 0.5*x+1
if x >= 2 and x < 6:
    print('Y = ',y)
    y = 0
if x >= 6:
    y = (x-6)**2
print('Y = ',y)