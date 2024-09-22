import numpy as np


# Определяем функцию f(x, y)
def f(x, y):
    return -3 * x**2 + 4 * y**2

# Функция для проверки, принадлежит ли точка области D
def in_D(x, y):
    return 0 <= y <= np.sin(np.pi * x / 2) + 1 and -1 <= x <= 1

# Функция для вычисления интегральных сумм на прямоугольной области
def calculate_rectangular_area(a, b, n):
    x = np.linspace(0, a, n + 1)
    y = np.linspace(0, b, n + 1)
    sums = {"lower_left": 0, "lower_right": 0, "upper_left": 0, "upper_right": 0, "center": 0, "random": 0}

    for i in range(n):
        for j in range(n):
            dx = x[i + 1] - x[i]
            dy = y[j + 1] - y[j]
            area = dx * dy

            # Различные углы и центр узлов сетки
            sums["lower_left"] += f(x[i], y[j]) * area
            sums["lower_right"] += f(x[i + 1], y[j]) * area
            sums["upper_left"] += f(x[i], y[j + 1]) * area
            sums["upper_right"] += f(x[i + 1], y[j + 1]) * area
            sums["center"] += f((x[i] + x[i + 1]) / 2, (y[j] + y[j + 1]) / 2) * area

            # Произвольная точка в узле сетки
            xi = np.random.uniform(x[i], x[i + 1])
            yi = np.random.uniform(y[j], y[j + 1])
            sums["random"] += f(xi, yi) * area

    return sums

# Функция для вычисления интеграла на непрямоугольной области детерминированным методом
def calculate_non_rectangular_area_deterministic():
    nx, ny = 100, 100
    sum_f = 0
    x_values = np.linspace(-1, 1, nx + 1)
    y_values = np.linspace(0, 2, ny + 1)

    for i in range(nx):
        for j in range(ny):
            xi = (x_values[i] + x_values[i + 1]) / 2
            yi = (y_values[j] + y_values[j + 1]) / 2

            if in_D(xi, yi):
                dx = x_values[i + 1] - x_values[i]
                dy = y_values[j + 1] - y_values[j]
                area = dx * dy
                sum_f += f(xi, yi) * area

    return sum_f

# Вычисление для прямоугольной области
a, b, n = 1, 1, 1000
rectangular_sums = calculate_rectangular_area(a, b, n)

# Вычисление для непрямоугольной области
non_rectangular_integral_deterministic = calculate_non_rectangular_area_deterministic()

# Вывод результатов
print("Результаты для прямоугольной области:", rectangular_sums)
print("Результат для непрямоугольной области:", non_rectangular_integral_deterministic)
