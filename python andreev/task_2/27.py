from math import *
x = float(input('input = '))
y = 0

if x <= -2.5:
    y = -0.5*x - 3
if x >= -2.5 and x <= 2:
    y = -1.279*10**-16*x**4+1*x**3+1.5*x**2-2.5*x-3
if x >= 2:
    y = -2*x+10
print('Y =',y)