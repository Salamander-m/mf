from random import *

m = []
k = 0
maximum = 0
s = []

row = int(input('input n of row = '))
line = int(input('input n of line = '))

def chet(massive):
    summ = 0
    for i in massive:
        if i >= 0 and i % 2 == 0:
            summ += i
    return(summ)

for i in range(row):
    a = []
    for j in range(line):
       a.append(randint(-10,10))
    m.append(a)
    if 0 not in a:
        k = k + 1

will_sorted = sorted(m,key=chet)
print('Отсортированный массив:',*will_sorted,sep='\n')
print('Количество строк, не содержащих ни одного нулевого элемента',k)