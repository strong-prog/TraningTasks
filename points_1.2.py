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
points = [(2, 5), (0, 2), (5, 2), (6, 6), (8, 3)]
matrix = []

# Создаем матрицу расстояний.
for i in range(len(points)):
    list_res = []
    for j in range(len(points)):
        result = ((points[j][0] - points[i][0]) ** 2 + (points[j][1] - points[i][1]) ** 2) ** 0.5
        list_res.append(round(result))
    matrix.append(list_res)

for m in matrix:
    print(m)
print()

# Вычисляем короткий путь по матрице.
min_dist = 10 ** 10
for p1 in range(len(matrix)):
    for p2 in range(len(matrix)):
        for p3 in range(len(matrix)):
            for p4 in range(len(matrix)):
                for p5 in range(len(matrix)):
                    if (p1 != p2 and p1 != p3 and p1 != p4 and p1 != p5
                            and p2 != p3 and p2 != p4 and p2 != p5 and p3 != p4 and p3 != p5 and p4 != p5):
                        dist = matrix[p1][p2] + matrix[p2][p3] + matrix[p3][p4] + matrix[p4][p5]
                        if dist < min_dist:
                            min_dist = dist
                            point_path = points[p1], points[p2], points[p3], points[p4], points[p5]
                            dist_point = matrix[p1][p2], matrix[p2][p3], matrix[p3][p4], matrix[p4][p5]

# Вычисляем рсстояние от последнего пункта до почты. Выводим результаты.
home_dist = ((point_path[-1][0] - point_path[0][0]) ** 2 + (point_path[-1][1] - point_path[0][1]) ** 2) ** 0.5

print(f'{point_path[0]} -> {point_path[1]}{[dist_point[0]]} -> {point_path[2]}{[dist_point[1]]} -> '
      f'{point_path[3]}{[dist_point[2]]} -> {point_path[4]}{[dist_point[2]]} -> {point_path[0]}{[home_dist]}'
      f' = {min_dist + home_dist}')
