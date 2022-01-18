from math import *
x = float(input('input = '))

if x <= -1:
    y = -x-1
if x >= -1 and x <= 1:
    y = 0
if x >= 1 and x <= 5:
    y = sqrt(4-(x-3)**2)
if x >= 5:
    y = -0.5*x+2.5
print('Y =',y)
