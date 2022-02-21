from re import I
from numpy import sort


n = input()
k = 0
summ = 0
for i in range(len(n)):
    if n[i] == '0' or n[i] == '1':
        k = k + 1
    else: 
        k = k - 1
l = len(n)
if k == l:
    for i in range(l):
        z = l - i - 1
        p = int(n[z])
        summ += p*(2**z)
print(summ)