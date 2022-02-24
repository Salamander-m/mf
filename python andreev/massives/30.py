from math import *
from random import *
m = []
x = []
y = []
s = []
n = int(input('input n = '))
for i in range(n):
    m.append(randint(-5,5))
for i in range(0,n,2):
    x.append(m[i])
    y.append(m[i+1])
x = sorted(x)
y = sorted(y)
print(x)
print(y)
for i in range(len(x)-1):
    rast = sqrt((x[i+1]-x[i])**2+(y[i+1]-y[i])**2)
    rast = abs(rast)
    s.append(rast)
s = sorted(s)
print(s)
