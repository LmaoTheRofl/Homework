import sympy as sp
import numpy as np


epsilon_0 = 8.85418781762039e-12
mu_0 = 4 * np.pi * 1e-7
c = 299792458
omega = 2.4e15
g = 2e-15  
epsilon_xx = 2.5
d = 0.05  # Толщина кристалла

ky, ex, ez = sp.symbols('ky ex ez', complex=True)

# Волновой вектор k
kappa_y = omega * sp.sqrt(epsilon_0 * mu_0)
k = sp.Matrix([0, ky, 0])

# Тензор диэлектрической проницаемости
epsilon = sp.Matrix([
    [epsilon_xx, 0, sp.I * g * kappa_y],
    [0, epsilon_xx, 0],
    [-sp.I * g * kappa_y, 0, epsilon_xx]
])

# Электрическое поле
E = sp.Matrix([ex, 0, ez])

# Уравнения для волновых векторов и поляризаций
eq1 = sp.Eq(-ky**2 * ex, mu_0 * omega**2 * (epsilon[0, 0] * ex + epsilon[0, 2] * ez))
eq2 = sp.Eq(-ky**2 * ez, mu_0 * omega**2 * (epsilon[2, 0] * ex + epsilon[2, 2] * ez))

# Решение уравнений для ky и E при условии ex != 0
solutions_ex = sp.solve([eq1.subs(ex, 1)], (ky, ez), dict=True)

# Решение уравнений для ky и E при условии ez != 0
solutions_ez = sp.solve([eq2.subs(ez, 1)], (ky, ex), dict=True)

# Объединение решений
solutions = solutions_ex + solutions_ez

print("1 и 2 пункты: Решение уравнения для волновых векторов ky и поляризаций e:")
for sol in solutions:
    print(sol)

# Определение фазовых скоростей
v_phi_1 = omega / sp.sqrt(epsilon_0 * mu_0 * (epsilon_xx - g * kappa_y))
v_phi_2 = omega / sp.sqrt(epsilon_0 * mu_0 * (epsilon_xx + g * kappa_y))

# Разность фазовых скоростей
delta_v = v_phi_1 - v_phi_2
print("\n3 пункт: Разность фазовых скоростей лучей с разной поляризацией:")
print(delta_v.evalf())

# Показатели преломления
n_1 = c / v_phi_1
n_2 = c / v_phi_2

# Угол поворота
Theta = (d * omega / (2 * c)) * (n_2 - n_1)
Theta_deg = Theta * (180 / sp.pi)  

print("\n4 пункт: Угол поворота плоскости поляризации:")
print(f"{Theta.evalf()} радиан ({Theta_deg.evalf()} градусов)")

# Фазовый сдвиг после первого прохождения
phase_shift_first_pass = (d * omega / c) * delta_v

# Фазовый сдвиг после отражения и второго прохождения
phase_shift_second_pass = 2 * phase_shift_first_pass

print("\n5 пункт: Фазовый сдвиг после первого прохождения и после отражения:")
print(f"Первый проход: {phase_shift_first_pass.evalf()}")
print(f"Второй проход: {phase_shift_second_pass.evalf()}")

print("\nВывод:")
print("При прохождении кристалла в первый раз сдвиг фаз между лево- и правополяризованными волнами равен", 
      f"{phase_shift_first_pass.evalf()} радиан ({Theta_deg.evalf()} градусов), т.е получим свет с линейной поляризацией.")
print("После повторного прохождения сдвиг фаз увеличится в два раза, но свет останется линейно поляризованным.")
