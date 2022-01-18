from math import *
x = int(input('input argument = '))

if x < -9:
    y = 0
if x > -6 and x < -3:
    y = x+3
if x == 6:
    y = -3
if x >= -9 and x < -6:
    y = -sqrt(9-(x+6)**2)
if x == -3:
    y = 0
if x > -3 and x < 0:
    y = sqrt(9-x**2)
if x == 0:
    y = 3
if x > 0 and x < 3:
    y = -x+3
if x == 3:
    y = 0
if x > 3 and x < 9:
    y = 0.5*x+1.5
print('Y = ',y)