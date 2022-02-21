from math import * 
x = float(input('input argument = '))
i = int(input('Введите номер задания = '))
if i == 1:
    if x < -9:
        y = 0
    if x > -6 and x < -3:
        y = x+3
    if x == 6:
        y = -3
    if x >= -9 and x < -6:
        y = -sqrt(9-(x+6)**2)
    if x == -3:
        y = 0
    if x > -3 and x < 0:
        y = sqrt(9-x**2)
    if x == 0:
        y = 3
    if x > 0 and x < 3:
        y = -x+3
    if x == 3:
        y = 0
    if x > 3 and x < 9:
        y = 0.5*x+1.5
 

if i == 2:
    if x <= -8:
        y = -3 
    if x > -8 and x <-3:
        y = 0.6*x+1.8
    if x == -3:
        y = 0
    if x > -3 and x < 3:
        y = -sqrt(9-x**2)
    if x >= 3 and x < 5:
        y = x-3
    if x == 5:
        y = 2
        print('Y = ',y)
        y = 3
    if x > 5 and x <= 8:
        y = 3

if i == 3: 
    if x >= -9 and x <= -5:
        y = -2 + sqrt(4 + (x+7)**2)
    if x >= -5 and x <= -4:
        y = 2
    if x >= -4 and x <= 0:
        y = x/-2
    if x >= 0 and x <= pi:
        y = (-4*x**2)/pi**2+(4*x/(pi))
    if x > pi and x <= 5:
        y = x-pi
  
if i == 4:
    if x <= 0:
        y = -0.5*x-3
    if x >= 0 and x <= 3:
        y = -sqrt(9-x**2)
    if x >= 3 and x <= 6:
        y = sqrt(9-(x-6)**2)
    print('Y = ',y)  
 
if i == 5:
    if x >= -4 and x <= -2:
        y = x + 3
    if x >= -2 and x <= 4:
        y = -0.5*x
    if x >= 4 and x <=6:
        y = -2
    if x >= 6 and x <= 10:
        y = -2 + sqrt(4 - (x-8)**2)
 
 
if i == 6:
    if x <= -5:
        y = -3
    if x <= -3 and x >= -5:
        y = x + 2
    if x >= -3 and x <= 3:
        y = sqrt(9-x**2)
    if x >= 3 and x <= 8:
        y = (3*x-9)/5
    if x >= 8:
        y = 3
 
 
if i == 7:
    if x <= -3:
        y = 3
    if x >= -3 and x <= 3:
        y = -3 + sqrt(9 - (x)**2)
    if x >= 3 and x <=6:
        y = (-6*x+27)/3
    if x >= 6:
        y = x - 9

if i == 8:
    if x <= -6:
        y = -2 + sqrt(4 - (x+8)**2)
    if x >= -6 and x <= 2:
        y = 0.5*x+1
    if x >= 2 and x < 6:
        print('Y = ',y)
        y = 0
    if x >= 6:
        y = (x-6)**2
  
if i == 9:
    if x >= -7 and x <= -3:
        y = x + 7
    if x == -2:
        y = 4
    if x >= -2 and x <= 2:
        y = x**2
    if x >= 2 and x < 4:
        y = -2*x+8
    if x >= 4:
        y = 0
 
if i == 10: 
    if x <= -6 and x >= -10:
        y = 2 - sqrt(4 - (x+8)**2)
    if x <= -4 and x >= -6:
        y = 2
    if x >= -4 and x <= 2:
        y = -0.5*x
    if x > 2:
        y = x-3
 
if i == 11:
    if x >= -3 and x <= -2:
        y = -(x+2)
    if x >= -2 and x <= -1:
        y = sqrt(1-(x+1)**2)
    if x >= -1 and x <= 1:
        y = 1
    if x >= 1 and x <= 2:
        y = -2*x+3
    if x >= 2:
        y = -1

if i == 12:
    if x < -6:
        y = 2
    if x >= -6 and x <= -2:
        y = (x+2)/4
    if x >= -2 and x <= 0:
        y = 2 - sqrt(4 - (x+2)**2)
    if x >= 0 and x <= 2:
        y = sqrt(4 - x**2)
    if x >= 2 and x <= 3:
        y = -x + 2
 
if i == 13:
    if x <= -3:
        y = -(x+3)
    if x >= -3 and x <= 0:
        y = sqrt(9-x**2)
    if x >= 0 and x <=6:
        y = -0.5*x+3
    if x >= 6:
        y = (x-6)
    
if i == 14:
    if x <= -4:
        y = -2
    if x >= -4 and x <= 0:
        y = 0.25*x
    if x >= 0 and x <= 2:
        y = x**2
    if x >= 2:
        y = (-4*x+40)/8

if i == 15: 
    if x >= -7 and x <= -6:
        y = 1
    if x >= -6 and x <= -4:
        y = -0.5*x - 2
    if x >= -4 and x <= 0:
        y = sqrt(4 - (x + 2)**2)
    if x >= 0 and x <= 2:
        y = -sqrt(1 - (x - 1)**2)
    if x >= 2:
        y = -x+2
 
 
if i == 16:
    if x <= -1:
        y = x + 2
    if x >= -1 and x <= 0:
        y = -1 + sqrt(1 - (x)**2)
    if x >= 0 and x <= 2:
        y = 2 - sqrt(4 - (x)**2)
    if x >= 2 and x <= 4:
        if x == 2:
            print('Y =',y)
        y = -1
    if x >= 4:
        y = 0.5*x-3

 
if i == 17:
    if x <= -3:
        y = 1
    if x >= -3 and x <= -1:
        if x == -3:
            print('Y =',y)
        y = -sqrt(4-(x+1)**2)
    if x >= -1 and x <= 2:
        y = -2
    if x >= 2:
        y = x - 4
 

if i == 18: 
    if x <= -2:
        y = -x-2
    if x >= -2 and x <= 0:
        y = sqrt(1 - (x+1)**2)
    if x >= 0 and x <= 4:
        y = -sqrt(4 - (x-2)**2)
    if x >= 4:
        y = -0.5*x+2
    if x >= 6:
        y = -1
  
 
if i == 19:
    if x <= -1:
        y = -x-1
    if x >= -1 and x <= 1:
        y = 0
    if x >= 1 and x <= 5:
        y = sqrt(4-(x-3)**2)
    if x >= 5:
        y = -0.5*x+2.5

if i == 20:  
    if x <= 0:
        y = -0.5*x
    if x >= 0 and x <= 2:
        y = 2-sqrt(4-(x)**2)
    if x >= 2 and x <= 4:
        y = 0+sqrt(4-(x-2)**2)
    if x>= 4:
        y = -0.5*x+2
  
if i == 21: 
    y = 0
    if x >= -4 and x <= 0:
        y = sqrt(4+(x+2)**2)
    if x >= 0 and x <= 0.5:
        y = 0
    if x >= 0.5 and x <=2:
        if x == 0.5:
            print('Y =',y)
        y = log(x)/x
    if x >= 2:
        if x == 2:
            print('Y =',y)
        y = 1

if i == 22:
    y = 0
    if x <= -2:
        y = -0.5*x + 1.5
    if x >= -2 and x <= 2:
        if x == -2:
            print('Y = ',y)
        y = 2*cos(2*x)
    if x >= 2:
        if x == 2:
            print('Y = ',y)
        y = 0.5*x - 1.5
print('Y =',y)  

if i == 23: 
    y = 0

    if x <= -2:
        y = 1/3*x+2/3
    if x >= -2 and x <= 2:
        if x == -2:
            print('Y =',y)
        y = tan(x/2)
    if x >= 2:
        if x == 2:
            print('Y =',y)
        y = 0.5*x-1.5

if i == 24: 
    y = 0
    if x <= -2:
        y = -1/3*x-2/3
    if x >= -2 and x <= 2:
        if x == -2:
            print('Y =',y)
        y = log(fabs(1/tan(x/2)))
    if x >= 2:
        if x == 2:
            print('Y =',y)
        y = 1/3*x-2/3


 


def ch(x):
    ans = 1/2*(e**(x)+e**(-x))
    return(-ans)
    
if i == 25:
    if x <=-5:
        y = 2
    if x >= -5 and x <= -1:
        y = 2 - sqrt(4-(x+3)**2)
    if x >= -1 and x <= 1:
        if x == -1:
            print('Y =',y)
        y = ch(x)
    if x >= 1 and x <= 2:
        if x == 1:
            print('Y =',y)
        y = 0
    if x >= 2 and x <= 4:
        y = sqrt(1 - (x-3)**2)
    if x >= 4:
        y = 0
  

if i == 26:
    y = 0

    if x <=-6:
        y = -2*x-14
    if x >= -6 and x <= -2:
        y = -2+sqrt(4-(x+4)**2)
    if x > -2 and x <= 2:
        y = log((2+x),2)
    if x >= 2 and x <= 4:
        if x == 2:
            print('Y =',y)
        y = sqrt(1-(x-3)**2)
    if x >= 4:
        y = 0
    print('Y =',y)  

if i == 27:
    y = 0

    if x <= -2.5:
        y = -0.5*x - 3
    if x >= -2.5 and x <= 2:
        y = -1.279*10**-16*x**4+1*x**3+1.5*x**2-2.5*x-3
    if x >= 2:
        y = -2*x+10
    
if i == 28:
    y = 0

    if x <= -6:
        y = 0
    if x >= -6 and x <= -2:
        y = 0.0193756*x**4+0.364141*x**3+1.4669*x**2-3.26446
    if x >= -2 and x <= 2:
        y = -sqrt(4-(x)**2)
    if x >= 2 and x < 8:
        y = log((x-1),2) #по графику видно, что y(8) = 2, хотя это невозможно при y = log(x-1,2)
    if x >= 8:
        y = -2*x+18
     
if i == 29:
    y = 0

    if x <= -3:
        y = x+3
    if x >= -3 and x <= 1:
        y = 3**x
    if x >= 1 and x <= 5:
        y = 3 - sqrt(4 - (x-3)**2)
    if x >= 5:
        y = -1.5*x+10.5
  
if i == 30:
    y = 0
    R = int(input('input R = '))
    if x <= -4:
        y = 2
    if x >= -4 and x <= -2:
        y = -R - sqrt(R**2-(x+2)**2)
    if x >= -2 and x <= 0:
        if x == -2:
            print('Y =',y)
        y = 0
    if x >= 0 and x <= 3:
        if x == 1:
            y = x
        else:
            k = 3 / (R+1)
            y = -k*x
    if x >= 3 and x <= 5:
        if x == 3:
            print('Y =',y)
        y = -1 + sqrt(R**2-(x-3)**2)
    if x >= 5:  
        y = -1
print('Y =',y)