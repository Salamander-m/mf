from math import *
x = float(input('input = '))
y = 0
if x <= -2:
    y = -1/3*x-2/3
if x >= -2 and x <= 2:
    if x == -2:
        print('Y =',y)
    y = log(fabs(1/tan(x/2)))
if x >= 2:
    if x == 2:
        print('Y =',y)
    y = 1/3*x-2/3

print('Y =',y)