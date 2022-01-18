# программа для вычисления значений для заданий 2
# а именно значений: b,k из y = kx + b
# и вывод уравнения окружности с вводимым центром окуржности

print('x1,x2')
x1 = int(input())
x2 = int(input())
print('y1,y2')
y1 = int(input())
y2 = int(input())

# y = kx + b
k = (y1 + y2)/(x1 - x2)
print('k =',k)

b = k*x1 - y1
print('b = ',b)


# (x-a)^2 + (y-b)^2 = R^2
print('R')
R = float(input())
print('centre R')
a = float(input())
b = float(input())
print('y = ',b,'+ sqrt(',R**2,'- (x -',a,')^2')
