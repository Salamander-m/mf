from math import *
from random import *
proz_1 = 1
proz_2 = 1
summ_neg = 0
summ_pos = 0
maxim = 0
n = int(input('input n = '))
m = []
# Вычисление отрицательных чисел из массива, который вводится рандомно
for i in range(n):
    m.append(uniform(-10,1))
m = sorted(m)
m_started = m[:]
m_abs = m[:]
for i in range(n):
    m_abs[i] = abs(m[i])
m_abs = sorted(m_abs)

for i in range(len(m)):
    if abs(m[i]) == max(m_abs):
        m.pop(i)
        break;
for i in range(len(m)):    
    if abs(m[i]) == min(m_abs):
        m.pop(i)
        break;
for i in range(len(m)):
    proz_2 *= m[i]
print('M =',m) 
print('Proz =',proz_2)           
print(m_abs)
print(max(m_abs))
print(min(m_abs))