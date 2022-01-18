from math import *
x = float(input('input argument = '))

if x <= -8:
    y = -3 
if x > -8 and x <-3:
    y = 0.6*x+1.8
if x == -3:
    y = 0
if x > -3 and x < 3:
    y = -sqrt(9-x**2)
if x >= 3 and x < 5:
    y = x-3
if x == 5:
    y = 2
    print('Y = ',y)
    y = 3
if x > 5 and x <= 8:
    y = 3
print('Y = ',y)