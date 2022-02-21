n = input()
k = 0
summ = 0
s = 0
ans = 0
l = len(n)
for i in range(l):
    z = l - i - 1
    if n[z] == 'A':
        p = 10
    elif n[z] == 'B':
        p = 11
    elif n[z] == 'C':
        p = 12
    elif n[z] == 'D':
        p = 13
    elif n[z] == 'E':
        p = 14
    elif n[z] == 'F':
        p = 15
    else:
        p = int(n[z])
    summ += p*(16**i)
print(summ)
while summ > 8:
    s = summ % 8
    summ = summ // 8
    ans += s * 10 ** k
    k = k + 1
ans += summ * 10 ** k
print(ans)