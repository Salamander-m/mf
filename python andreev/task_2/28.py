from math import *
x = float(input('input = '))
y = 0

if x <= -6:
    y = 0
if x >= -6 and x <= -2:
    y = 0.0193756*x**4+0.364141*x**3+1.4669*x**2-3.26446
if x >= -2 and x <= 2:
    y = -sqrt(4-(x)**2)
if x >= 2 and x < 8:
    y = log((x-1),2) #по графику видно, что y(8) = 2, хотя это невозможно при y = log(x-1,2)
if x >= 8:
    y = -2*x+18
print('Y =',y)