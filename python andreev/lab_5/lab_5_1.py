from math import *
from random import *
m = []
k = 0
z = 0
maximum = 0
row = int(input('input n of row = '))
line = int(input('input n of line = '))
for i in range(row):
    a = []
    for j in range(line):
        a.append(uniform(-5,5))
    m.append(a)
    if 0 not in a:
        k = k + 1
    b = sorted(a,reverse=True)
    z = 0
    for j in range(line):
        if b[j] >= maximum:
            z = z + 1
            maximum = b[j]
print('Количество повторяющего максимума',z)
print('Количество строк, не содержащих ни одного нулевого элемента',k)
print(*m,sep='\n')
