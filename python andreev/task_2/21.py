from math import *
x = float(input('input = '))
y = 0
if x >= -4 and x <= 0:
    y = sqrt(4+(x+2)**2)
if x >= 0 and x <= 0.5:
    y = 0
if x >= 0.5 and x <=2:
    if x == 0.5:
        print('Y =',y)
    y = log(x)/x
if x >= 2:
    if x == 2:
        print('Y =',y)
    y = 1
print('Y =',y)