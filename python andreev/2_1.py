from math import *
from random import *
m = []
row = int(input())
line = int(input())
for i in range(row):
    a = []
    for j in range(line):
        a.append(uniform(-5,5))
    m.append(a)
print(m)