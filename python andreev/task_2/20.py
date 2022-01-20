from math import *
x = float(input('input = '))

if x <= 0:
    y = -0.5*x
if x >= 0 and x <= 2:
    y = 2-sqrt(4-(x)**2)
if x >= 2 and x <= 4:
    y = 0+sqrt(4-(x-2)**2)
if x>= 4:
    y = -0.5*x+2
print('Y =',y)