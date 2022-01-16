from re import X


print('x1,x2')
x1 = int(input())
x2 = int(input())
print('y')
y = int(input())
print('R')
R = int(input())

k = (x2-x1)/y
print(k)
# y = kx + b
# (x-a)^2 + (y-b)^2 = R^2
print('centre R')
a = int(input())
b = int(input())
print('y = ',b,'+ sqrt(',R**2,'- (x -',a,')')
