from random import *

m = []
k = 0
maximum = 0
s = []

row = int(input('input n of row = '))
line = int(input('input n of line = '))

def chet(massive):
    count = 0
    same = 0
    for i in massive:
        if i == same:
            count += 1
    return(count)

for i in range(row):
    a = []
    for j in range(line):
       a.append(randint(-1,1))
    m.append(a)
    if 0 in a:
        k = k + 1
    s.append(chet(a))
print(*m,sep='\n')
print('Максимальное количество подряд идущих элементов в строке',max(s))
print('Количество строк, содержащих хотя бы однин нулевой элемент',k)