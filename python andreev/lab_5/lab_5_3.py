from random import *
from collections import Counter

m = []
k = 0
maximum = 0
s = []

row = int(input('input n of row = '))
line = int(input('input n of line = '))

for i in range(row):
    a = []
    for j in range(line):
       a.append(randint(0,5))
    b = Counter(a)
    c = b.values()
    for i in c:
        s.append(i)
    m.append(a)
    if 0 in a:
        k = k + 1
print(*m,sep='\n')
print('Максимальное количество подряд идущих элементов в строке',max(s))
print('Количество строк, содержащих хотя бы однин нулевой элемент',k)
