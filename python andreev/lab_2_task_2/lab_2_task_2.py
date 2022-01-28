from math import *
import csv

q = input('Выводить изначальное изображение? Y/N ')
q = q.lower()

#Вывод csv файла с списком заданий
with open("python andreev\lab_2_task_2\\tasks.csv", encoding='utf-8') as r_file:
    # Создаем объект DictReader, указываем символ-разделитель ","
    count = 0
    # Счетчик для подсчета количества строк и вывода заголовков столбцов
    file_reader = csv.DictReader(r_file, delimiter = ",")
    # Считывание данных из CSV файла
    print(f'Список выполненных заданий с их кратким описанием')
    for row in file_reader:
        # Вывод строк
        print(f' #{row["Задание"]} - {row["Краткое описание"]}', end='')
        print(f' ')
        # Счётчик для последуйщей проверки значений
        count += 1
count = int(count)

# Здесь начинается ~magic~
# Бесконечный цикл позволяет нам смотреть все интересующие нас задания пока не надоест 
while(True):
    task = int(input('Введите номер задания: '))
    # Вывод изображения задания через matlotlib их директории tasks
    if q == 'y':
        from matplotlib import pyplot as plt
        img = plt.imread(f"python andreev\lab_2_task_2\\tasks\{task}.png")
        plt.imshow(img)
        plt.show()
    
    while(task > count):
        task = int(input('Такого номера нет в списке, введите снова = '))
        if task <= count:
            break;
        else:
            continue;
    if task <= count:
        x = float(input('input x = '))
        y = float(input('input y = '))
        R = float(input('input R = '))
        ans = ''
        check = 0
    if task == 1:
    #--------1--------
    # y = kx == R
    # 2 = kx
    # 1 <= x,y <= sin(pi/2)/2 

        if (x <= 0 and y <= 0):
            if ((y >= -sqrt(R**2-x**2) and y <= x) and x >= -2*sin(pi/4)/2*R): 
                ans = 'yes'
            #сравнение y(х) с значением функции окружности, которое берется как максимальное значение для y(x)
            #а х сравнивается с максимумом функкции y = kx 
        elif (x >= 0 and y >= 0):
            if ((y <= sqrt(R**2-x**2) and y >= x) and x <= 2*sin(pi/4)/2*R):
                ans = 'yes'
        else:
            ans = 'no'
        print(ans)


    elif task == 2:
    #--------2--------


        if (x <= 0 and y >= 0):
            if x <= R and y <=R:
                z = sqrt(R**2-x**2)
                print(z)
                if y <= round(z,1):
                    ans = 'yes'
                    #сравнение y(x) с уравнением окружности и устанавливается предел допустимых значений y для х
                else:
                    ans = 'no'
        elif (x >= 0 and x <= R) and y <= 0:
            z = R*x-R**2
            z = round(z,1)
            w = -R*x
            print(w,z)
            if (x == R and y != 0) or x > R:
                ans = 'no'
            else:
                if z <= y or y == w or q <= y:
                    ans = 'yes'
                    #треугольник представлен как функции y= -2x(w),y = R*x-R**2(z), x = 0
        else:
            ans = 'no'
            print(ans)

    elif task == 3:
    #--------3--------
    #check = самое тупое до чего я когда-то додумался
    #если предыдущее условие сработало - дальше программа не идет xD
        half_of_R = R/2
        if x >= -R/2 and x <= R/2:

            if x <= 0:
                #equation_cirle_one -> (x-(R/2)**2) + (y+(R/2)**2) = (R/2)**2
                y_circle_up = (half_of_R) - sqrt((half_of_R)**2 - (x+(half_of_R))**2)
            
            if x >= 0:
                #equation_circle_two -> (x+(R/2)**2) + (y-(R/2)**2) = (R/2)**2
                y_circle_down = -(half_of_R) + sqrt((half_of_R)**2 - (x-(half_of_R))**2)
        else:
            ans = 'no'
            check += 1       
        #дальше нужно было использовать elif, но если работает не трожь?
        if check == 0 and x > 0 and y >= y_circle_down and y <= R/2:
            ans = 'yes'
            check += 1

        if check == 0 and x < 0 and y <= y_circle_up and y >= -R/2:
            ans = 'yes'
            check += 1

        if  check == 0 and x == 0 and y >= -R/2 and y <= R/2:
            ans = 'yes'
            check += 1

        if check == 0:
            ans = 'no'
        print(ans)


    elif task == 4:
    #--------4--------
        if x > R or x < -R:
            ans = 'no'
        else:
            # Вычисление максимального допустимого значения для окружности
            check = sqrt(R**2-x**2)
            # Вычисление уравнения прямой
            straight = R
            if y >= 0:
                # Сравнение с крайним значением
                if y <= check:
                    ans = 'yes'
            elif (y <= x and x <= 0 and y >= -straight):
                ans = 'yes'
            else:
                ans = 'no'
        print(ans)
    

    elif task == 5:
    #--------19--------
        #equation_square -> fabs(x+y)+fabs(x-y) = R 
        #equation_circle_one -> sqrt(R**2-x**2)
        #equation_triangle -> y = -x-2*R and x = 0 and y = 0
        check = sqrt(R**2-x**2)
        straight = -x - 2*R
        if x >= 0 and y >= 0:
            if y >= check and y <= 2*R and x <= 2*R:
                ans = 'yes'
        elif x <= 0 and y <= 0:
            if y <= 0 and y >= straight and x >= -2*R and y >= -2*R:
                ans = 'yes'
        else:
            ans = 'no' 
        print(ans)

    
    elif task == 6:
    #--------26--------
    # Окружность и 2 квадрата со стороной R
        # Высчитывается формула окружности
        check = sqrt(R**2-x**2)
        # Округление значение до сотых
        check = round(check,3)
        # Вычисления уравнения прямой
        straight = x + R
        # Первая четверть
        if x >= 0 and y >= 0:
            if (y >= check and y <= R and x <= R) or (x == R and y <= R):
                ans = 'yes'
        # Четвертая четверть
        elif x >= 0 and y <= 0:
            if y <= check and x <= check:
                ans = 'yes'
        # Третья четверть
        elif x <= 0 and y <= 0:
            if (y <= -check and y >= -R and x >= -R) or (x == -R and y >= -R):
                ans = 'yes'
        # Вторая четверть
        elif x <= 0 and y >= 0:
            if (y >= straight and y <= check and x >= -R):
                ans = 'yes'
        else:
            ans = 'no'
        print(ans)

    # Очереденой бесконечный цикл бесконечно спрашивающий хотите ли продолжить
    while(True):
        # Ввод текста
        ques = str(input('Хотите продолжить? Y/N: '))
        # Текст принимает одиннаковый регистр
        ques = ques.lower()
        # Если вводится (N,n) - продолжает спрашивает
        if ques == 'n':
            exit()
        # Если вводится (Y,y) - возвращает к первому while(True)
        elif ques == 'y':
            break;
        else:
            continue;
        
