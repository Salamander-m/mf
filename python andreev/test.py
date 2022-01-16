import math
a = input()
a = int(a)
pi = math.pi

z1 = math.cos(a)+math.sin(a)+math.cos(3*a)+math.sin(3*a)
z2 = 2*math.sqrt(2)*math.cos(a)*math.sin(math.pi/4+2*a) #2

z1 = (math.sin(2*a)+math.sin(5*a)-math.sin(3*a))/(math.cos(a)+1-2*math.sin(2*a)**2)
z2 = 2*math.sin(a) #3

z1 = (2*math.cos(a)*math.sin(2*a) - math.sin(a)) / (math.cos(a) - 2*math.sin(a) * math.sin(2*a))
z2 = math.tan(3*a) #4

z1 = math.cos(a) + math.cos(2*a) + math.cos(6*a) + math.cos(7*a) #6
z2 = 4*math.cos(a/2) * math.cos(5/2*a) * math.cos(4*a)

z1 = 1 - 1/4*math.sin(2*a)**2+math.cos(2*a) #5
z2 = math.cos(a)**2+math.cos(a)**4

b = int(input())
z1 = (math.sin(a) + math.cos(2*b-a)) / (math.cos(a) - math.sin(2*b-a)) #13
z2 = (1 + math.sin(2*b)) / math.cos(2*b)

z1 = (math.cos(a) + math.sin(a)) / (math.cos(a) - math.sin(a)) #14
z2 = math.tan(2*a)+ 1/math.cos(2*a)

z1 = (math.sqrt(2*b+2*math.sqrt(b**2-4))) / (math.sqrt(b**2-4)+b+2)
z2 = 1/math.sqrt(b+2) #15

z1 = (a**2 + 2*a - 3 + (a+1) * math.sqrt(a**2-9)) /  (a**2 - 2*a - 3 + (a-1) * math.sqrt(a**2-9))
z2 = math.sqrt(a+3)/math.sqrt(a-3) #16

z1 = ((a-1)*math.sqrt(a)-(b-1)*math.sqrt(b)) / (math.sqrt(a**3*b)+b*a+a**2-a)
z2 = (math.sqrt(a) - math.sqrt(b)) / a #20

z1 = (1 + math.sin(-a)**4 - math.cos(-a)**4) / math.cos(a)**2
z2 = 2*math.tan(a)**2 #21

z1 = (math.tan(a - pi/2)*math.cos(3*pi/2 + a) - math.sin(7*pi/2 - a)**3) / (math.cos(a - pi/2) * math.tan(3*pi/2 + a))
z2 = math.sin(a)**2 #26

z1 = a**math.sqrt(math.log(b,a)) - b**math.sqrt(math.log(a,b)) + math.tan(a*b+3*pi/2)
z2 = math.tan(a*b + 3*pi/2) #27

z1 = (math.sin(a)**2 - math.tan(a)**2) / (math.cos(a)**2 - (math.cos(a)/math.sin(a))**2)
z2 = math.tan(a)**6 #28

z1 = (1 - 2*math.sin(a)**2) / (2*(math.cos(pi/4+a)/math.sin(pi/4+a))*math.cos(pi/4-a)**2) + math.e**a
z2 = 1 + math.e**a #29

z1 = (math.sin(a)**4 + 2*math.sin(a)*math.cos(a) - math.cos(a)**4) / (math.tan(2*a) - 1)
z2 = math.cos(2*a) #30
print(z1)
print(z2)
