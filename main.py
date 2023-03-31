import csv
import re


#1. Парсим csv в двумерный массив
with open("task.csv", encoding="utf-8") as file:
    file_read = csv.reader(file)
    array = list(file_read)

print("Исходная таблица:")
for line,_line in enumerate(array):
    for col, _element in enumerate(_line):
        l = len(str(array[line][col]))
        print(array[line][col], end = '')
        if l < 11:
            print(' '* (11-l), end = '')
        else:
            print(' '*(50-l), end = '')
    print()


print("\nТаблица со значениями в секундах:")
#2. Приведём все значения к секундам
for line,_line in enumerate(array[1:], start=1):
    print(line, end='')
    if line < 10: print(' '*8, end='')
    else: print(' '*7, end='')

    for col, _element in enumerate(_line[1:], start=1):
        # Заранее проверим, есть ли среди ячеек пустые значения и заменим их на 0
        if type(_element) != str:
            array[line][col] = 0

        try:
            if re.fullmatch("\d\d:\d\d:\d\d", _element):
                array[line][col] = (int(_element[:2])*3600 + int(_element[3:5])*60 + int(_element[6:]) )
            elif re.fullmatch("\d\d:\d\d", _element):
                array[line][col] = (int(_element[:2])*3600 + int(_element[3:]) * 60 )
            elif re.fullmatch("\d:\d\d", _element):
                array[line][col] = (int(_element[:1]) * 3600 + int(_element[2:]) * 60)
        except TypeError:
            array[line][col] = 0

        # Сейчас у нас всё приведено к одной единице измерения и устранены пустые значения (заменены на 0)

        # Выведем таблицу с приведёнными к сантиметрам значениями
        if array[line][col] == 0: print("\033[43m", end = '')

        l = len(str(array[line][col]))
        print(array[line][col], end = '')
        print(' '* (5-l), end = '')
        print('\033[0m', end = '')
        print(' '*4, end = '')
    print()

#3. Теперь определим координаты нулей в массиве
mis_data = []

for line,_line in enumerate(array[1:], start=1):
    for col, _element in enumerate(_line[1:], start=1):
        if _element == 0: mis_data.append((line, col))

#4. Определим величину пропущенного интервала
difference_real = array[(mis_data[-1][0])+1][mis_data[-1][1]] - array[(mis_data[0][0])-1][mis_data[0][1]]
print(f"Пропущенный интервал: {difference_real} секунд(ы)")

#5. Определим время прохождения остановок в других столбцах

lod = []

def raz(stroka, n, mis_data):
    a = []
    for col, _element in enumerate(stroka[1:], start=1):
        if col != mis_data[0][1]:
            razn = array[n][col]-array[n-1][col]
            a.append(razn)
    return a

for line, _line in enumerate(array[1:], start=1):
    for i in mis_data:
        if line == i[0]:
            lod.append(raz(_line, line, mis_data))


# Также найдём интервалы между следующей после последней и последней строками
external = []
for time,_time in enumerate(array[mis_data[-1][0]+1]):
    if time != 0 and time != mis_data[0][1]:
        external.append(_time-array[mis_data[-1][0]][time])

# В lod интервалы хранятся построчно: каждый вложенный массив соответствует каждой строке

#6. Теперь определим means полученных значений
l = len(lod[0])

means = []
for i in lod:
    summa = 0
    for j in i:
        summa += j
    summa = summa/l
    means.append(summa)

ex_sum = 0
for i in external:
    ex_sum += i
ex_mean = ex_sum/l

#7. Просуммируем means
difference_means = round(sum(means)+ex_mean)
print(f"Сумма средних значений: {difference_means} секунд(ы)")

# Они не верили, что я смогу сделать это без pandas... Всё готово для последнего шага ###

#8. Предполагаемая величина пропущенных интервалов (в секундах)

print("\nПредполагаемая величина пропущенных интервалов (в секундах):")
result = []
for i in means:
    tmp = difference_real*i/difference_means
    result.append(tmp)
    print(round(tmp))

#9. Прибавим интервалы к последнему известному значению, чтобы наконец-то узнать то, что нам нужно
print("\nОтветики:")
time = array[mis_data[0][0]-1][mis_data[0][1]] 
for i in result:
    time += i
    answer = time
    hh = round(answer//3600)
    answer -= hh*3600
    if hh <10: hh = "0"+str(hh)
    mm = round(answer//60)
    answer -= mm*60
    if mm <10: mm = "0"+str(mm)
    ss = round(answer)
    if ss <10: ss = "0"+str(ss)
 
    print(f"{hh}:{mm}:{ss}")
    

print("\n\nС любовью, @greg_zamza <3")
