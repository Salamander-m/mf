from random import *

m = []
summ_main = 0
summ = 0
s = 0
proiz = 1
otvet = []

row = int(input('input n of row = '))
line = row

def chet(i,j,m): 
    l = m[i]
    return(l[j])

for i in range(row):
    k = 0
    a = []
    for j in range(line):
        a.append(randint(-5,10))
    for n in a:
        if n > 0:
            k += 1
    if k == row:
        for n in a:
            proiz *= n
    m.append(a)

for s in range(row):
    i = 0
    summ = 0  
    while i != row and s != row:
        summ += chet(i,s,m)
        i += 1
        s += 1
    otvet.append(summ)
for i in range(1,row):
    s = 0
    summ = 0  
    while i != row and s != row:
        summ += chet(i,s,m)
        i += 1
        s += 1
    otvet.append(summ)
otvet.pop(0)
print('Проивездение строк с положительными элементами =',proiz)
print('Максимум среди сумм элементов диагоналей, параллельных главной =',max(otvet))
print(*m,sep='\n')