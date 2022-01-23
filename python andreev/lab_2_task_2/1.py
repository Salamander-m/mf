from math import *
x = float(input('input x = '))
y = float(input('input y = '))
R = float(input('input R = '))
ans = ''
# y = kx == R
# 2 = kx
# 1 <= x,y <= sin(pi/2)/2 

#1
'''
if (x >= 0 and y >= 0) or (x <= 0 and y <= 0):
    if (x <= sin(pi/4)/2*R and x >= -sin(pi/4)/2*R) and (y >= -R and y <= R):
        ans = 'yes'
'''
#2
if (x <= 0 and y >= 0):
    if x <= R and y <=R:
        z = sqrt(R**2-x**2)
        if y == round(z,1) or y == -x:
            ans = 'yes'
        else:
            ans = 'no'
if (x >= 0 and x <= R) and y <= 0:
    z = R*x-R**2
    z = round(z,1)
    w = -R/2*x
    print(w,z)
    if x == R and y != 0:
        ans = 'no'
    else:
        if z == y or y == w:
            ans = 'yes'
        else:
            ans = 'no'
print(ans)