from math import *
from turtle import end_fill, st
import os
task = str(input('Input number of task = '))

if task == '1':
    print('Условия существования функции |x| > 1')
if task == '4':
    print('Условия существования функции -1<x<=1')
if task == '5':
    print('Условия существования функции |x| < 1')
if task == '6':
    print('Условия существования функции -1<=x<1')

print('Введите Xbeg, Xend, Dx и Точность (целочисленную)') 
xb = float(input('Xbeg = '))
xe = float(input('Xend = ')) 
dx = float(input('Dx = '))
# ТОЧНОСТЬ ВВОДИТЬ ЦЕЛОЧИСЛЕННУЮ, ОПРЕДЕЛЯЕТ КОЛИЧЕСТВО ЗНАКОВ ПОСЛЕ ЗАПЯТОЙ У ЗНАЧЕНИЯ ФУНКЦИИ 
eps = int(input('Eps = '))
print("+        +       +       +") 
print("I   X    I   N   I   Y   I") 
print("+        +       +       +") 
xt = xb
ans = 0
n = 0
#----0----
# Функция распечатывания таблички
def pechat(x,n,y):
    print('I   ',end = '')
    print(x, end = '  I   ')
    print(round(n,eps),end='   I   ')
    print(round(y,eps),end = '')
    print()
#----1----
def fonk1(x):
    if x == 1:
        print('Введено значение не принадлежащее отрезку функции')
        exit()
    else:
        y = 0
        global n
        y_original = log((x+1)/(x-1))
        y = 1/((2*n+1)*x**(2*n+1))
        while round(y,2) != round(y_original,2):
            y = 1/((2*n+1)*x**(2*n+1))
            if y > y_original:
                n += 0.001
            if y < y_original:
                n -= 0.001 

        pechat(x,n,y)
#----2----
def fonk2(x):
    y = 0
    n = 1
    y_original = e**(-x)
    y = ((-1)**n * x **n) / factorial(n)
    while round(y,1) != round(y_original,1):
        y = ((-1)**n * x **n) / factorial(n)
        if abs(y) > abs(y_original):
            n += 1
        if abs(y) < abs(y_original):
            n -= 1
    pechat(x,n,y)
#----3----
def fonk3(x):
    y = 0
    n = 0
    while n < x:
        y = x**n / factorial(n)
        n += 1
    pechat(x,n,y)
#----4----
# -1<x<=1 -> x > -1 and x <= 1 
def fonk4(x):
    if x <= 1 and x > -1:
        y = 0
        global n
        n += 1
        y = log(1+x)*(-1)**n  
        pechat(x,n,y)   
    else:
        print('Введено значение не принадлежащее отрезку функции')
        exit()

#----5----
# |x| < 1
def fonk5(x):
    if abs(x) < 1:
        y = 0
        global n
        n += 1
        y = (log(1+x) / log(1-x))
        pechat(x,n,y)
    else:
        print('Введено значение не принадлежащее отрезку функции')
        exit()
#----6----
def fonk6(x):
    if x < 1 and x >= -1:
        y = 0
        global n
        n += 1
        y = log(1-x)
        pechat(x,n,y)
    else:
        print('Введено значение не принадлежащее отрезку функции')
        exit()


while xt <= xe:
    # Использование глобального списка имен для подключения необходимой функции ФОНК
    y = globals()['fonk'+task](xt)
    #print("I ",xt," I ",round(y,eps)," I ",n," I ") 
    xt = xt + dx
 
