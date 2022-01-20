from math import *
x = float(input('input = '))
y = 0

if x <= -2:
    y = 1/3*x+2/3
if x >= -2 and x <= 2:
    if x == -2:
        print('Y =',y)
    y = tan(x/2)
if x >= 2:
    if x == 2:
        print('Y =',y)
    y = 0.5*x-1.5
print('Y =',y)