from math import *
x = float(input('input = '))
y = 0

if x <= -3:
    y = x+3
if x >= -3 and x <= 1:
    y = 3**x
if x >= 1 and x <= 5:
    y = 3 - sqrt(4 - (x-3)**2)
if x >= 5:
    y = -1.5*x+10.5
print('Y =',y)