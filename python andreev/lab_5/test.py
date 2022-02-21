from math import *
x = int(input())
n = 1
y_original = e**(-x)
y = ((-1)**n * x **n) / factorial(n)
print(round(y,1))
print(round(y_original,1))
while round(y,1) != round(y_original,1):
    y = ((-1)**n * x **n) / factorial(n)
    if abs(y) > abs(y_original):
        n += 1
    if abs(y) < abs(y_original):
        n -= 1
print(round(n,3))
    