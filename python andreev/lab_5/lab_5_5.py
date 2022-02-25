from random import *
from math import *
m = []
summ = 0
k = 0
otvet = []

row = int(input('input n of row = '))
line = row

def chet(i,j,m):
    l = m[i]
    return(l[j])

for i in range(row):
    a = []
    for j in range(line):
       a.append(randint(-1,10))
    m.append(a)

j = 0
while j != line:
    k = 0
    summ = 0
    for i in range(row):
        if chet(i,j,m) >= 0:
            k += 1
    if k == row:
        for i in range(row):
            if chet(i,j,m) >= 0:
                summ += chet(i,j,m)
    if summ != 0:
        print(f'Сумма столбца с положительными значениями (столбец {j+1}) =',summ)
    j += 1
for s in range(0,row):
    i = row-1
    summ = 0  
    while i != -1 and s != row :
        summ += abs(chet(i,s,m))
        i -= 1
        s += 1
    otvet.append(summ)
for i in range(0,row-1):
    summ = 0 
    s = 0
    while s != -1 and i != -1:
        summ += abs(chet(i,s,m))
        i -= 1
        s += 1
    otvet.append(summ)
print('Минимум сумм модулей элементов диагоналей, параллельных побочной диагонали',min(otvet))
print(*m,sep='\n')
