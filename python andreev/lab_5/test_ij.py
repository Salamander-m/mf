m = [[9,1,6],[0,4,5],[1,3,5]]
i = 0
j = 1
s = 0
n = 0

# m[i] = [9,1]
l = m[i]
def chet(i,j,m): 
    l = m[i]
    return(l[j])
for s in range(3):
    summ = 0
    n = 0
    print('----')
    while n != 3 and s != 3:
        summ += chet(n,s,m)
        s += 1
        n += 1
    print(summ)
for i in range(2):
    print(i)