from math import *
x = float(input('input = '))
y = 0
if x <= -2:
    y = -0.5*x + 1.5
if x >= -2 and x <= 2:
    if x == -2:
        print('Y = ',y)
    y = 2*cos(2*x)
if x >= 2:
    if x == 2:
        print('Y = ',y)
    y = 0.5*x - 1.5
print('Y =',y)