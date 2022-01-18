from math import *
x = float(input('input = '))

if x <= -1:
    y = x + 2
if x >= -1 and x <= 0:
    y = -1 + sqrt(1 - (x)**2)
if x >= 0 and x <= 2:
    y = 2 - sqrt(4 - (x)**2)
if x >= 2 and x <= 4:
    if x == 2:
        print('Y =',y)
    y = -1
if x >= 4:
    y = 0.5*x-3
print('Y = ',y)