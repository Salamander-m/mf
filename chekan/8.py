a = int(input('введите диф(0) или анн(1) система: '))

price = int(input('Сумма кредита: '))
summ_first = int(input('Первый взнос: '))
year_percent = float(input('Годовой процент: '))
count = int(input('Количество месяцев: '))
den = 30

price = price - summ_first
year_percent = year_percent/ 100 
if a == 1:
    year_percent = year_percent / 12
    kef = (year_percent * (1+year_percent)**count) / ((1+year_percent)**count - 1)
    ans = price * kef
    print('Ежемесячная оплата по аннуитетной системе =',ans)
if a == 0:
    kef = price / count
    dolg = price * year_percent * den / 365 
    dolg += kef
    for i in range(count):
        if den == 30:
            den += 1
            dolg = price * year_percent * den / 365 
            dolg += kef
            price = price - dolg
            print(f'{i+1} месяц =',round(dolg,2))
        elif den == 31:
            den -= 1
            dolg = price * year_percent * den / 365 
            dolg += kef
            price = price - dolg
            print(f'{i+1} месяц =',round(dolg,2))

