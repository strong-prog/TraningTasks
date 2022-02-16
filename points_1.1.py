"""
Описание задачи:
Почтальон выходит из почтового отделения, объезжает всех адресатов один раз
для вручения посылки и возвращается в почтовое отделение.
Необходимо найти кратчайший маршрут для почтальона.

Требования к выходным данным:
Результат выполнения программы должен содержать последовательность точек,
которые составляют самый короткий из маршрутов с выводом промежуточных расстояний
для каждой точки (от начала до текущей точки) и общей длины маршрута.
"""

# Программа для вычисления кратчайшего пути для почтальона по оси x,y.
points = [(2, 5), (5, 2), (6, 6), (8, 3)]
start = (0, 2)
dict_points = {}
num = 1
start_point = start

# Вычисляем, определяем и добавляем минимальное расстояние, и пункт.
while True:
    min_dist = 10 ** 10
    for point in points:
        result = ((point[0] - start_point[0]) ** 2 + (point[1] - start_point[1]) ** 2) ** 0.5
        if result < min_dist:
            min_dist = result
            new_start_point = point

    points.remove(new_start_point)
    dict_points[num] = new_start_point, min_dist
    start_point = new_start_point
    num += 1

    if len(points) == 0:
        last_point = new_start_point
        break

# Вычисляем рсстояние от последнего пункта до почты. Выводим результаты.
home_dist = ((last_point[0] - start[0]) ** 2 + (last_point[1] - start[1]) ** 2) ** 0.5
dict_points[num] = start, home_dist
total = 0
print(f'{start} ->', end=' ')
for keys in dict_points:
    total += dict_points[keys][1]
    if keys != len(dict_points):
        print(f'{dict_points[keys][0]}{[dict_points[keys][1]]} ->', end=' ')
    else:
        print(f'{dict_points[keys][0]}{[dict_points[keys][1]]} = {total}', end=' ')
