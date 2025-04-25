import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import time
import sympy as sp
from scipy.misc import derivative
import ast

x = sp.symbols('x')
y = sp.symbols('y')

    
def z_func(x,y):
    return ((1-x)**2 + 100*((y-(x**2))**2)) # произвольная функция

eq1 = sp.Eq(sp.diff(z_func(x, y), x), 0)
eq2 = sp.Eq(sp.diff(z_func(x, y), y), 0)

solutions = str(sp.solve([eq1, eq2], (x, y)))
value = ast.literal_eval(solutions)
solx, soly = value[0]
print('x = '+str(solx))
print('y = '+str(soly))
result = z_func(solx, soly)
print('z = '+str(result))

matrix = [[sp.diff(sp.diff(z_func(x, y), x), x),sp.diff(sp.diff(z_func(x, y), y), x) ], [sp.diff(sp.diff(z_func(x, y), x), y), sp.diff(sp.diff(z_func(x, y), y), y)]]
print('Матрица Гессе')
print(matrix)
A = (sp.diff(sp.diff(z_func(x, y), x), x).subs([(x, solx), (y, soly)]))
B = (sp.diff(sp.diff(z_func(x, y), y), x).subs([(x, solx), (y, soly)]))
C = (sp.diff(sp.diff(z_func(x, y), y), y).subs([(x, solx), (y, soly)]))
matrixval = [[sp.diff(sp.diff(z_func(x, y), x), x).subs([(x, solx), (y, soly)]),sp.diff(sp.diff(z_func(x, y), y), x).subs([(x, solx), (y, soly)]) ], [sp.diff(sp.diff(z_func(x, y), x), y).subs([(x, solx), (y, soly)]), sp.diff(sp.diff(z_func(x, y), y), y).subs([(x, solx), (y, soly)])]]
print('Матрица Гессе для точки')
print(matrixval)
print('A = '+str(A))
print('B = '+str(B))
print('C = '+str(C))
if A*C - B**2 > 0 and A > 0:
    print(' A*C - B**2 > 0 и A > 0: в точке '+'('+str(solx)+', '+str(soly)+', '+str(result)+')'+' имеется минимум')
elif A*C - B**2 > 0 and A < 0:
    print(' A*C - B**2 > 0 и A < 0: в точке '+'('+str(solx)+', '+str(soly)+', '+str(result)+')'+' имеется максимум')
elif A*C - B**2 < 0:
    print(' A*C - B**2 < 0: точка '+'('+str(solx)+', '+str(soly)+', '+str(result)+')'+' не является точкой экстремума')


x = np.arange(-2.0,2.0,0.01)
y = np.arange(-2.0,2.0,0.01)
X,Y = np.meshgrid(x, y) 
Z = z_func(X, Y) 
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
surf = ax.plot_surface(X, Y, Z, rstride=1,
                      cmap=cm.RdBu)
ax.scatter([1], [1], [0], color='black', s=10)
plt.show()

#начальное приращение
dx = 0.1 
dy = 0.1 
#начальные координаты
x = 0.1 
y = 0.1 
fP = z_func(x, y) 
#разница значений функции на текущей итерации
df = 1
# learning rate
a = 0.00001 

i = 0
lX = []
lY = []
lZ = []
start_time = time.time()
while np.abs(df) > 0.00000001 and np.sqrt((dx)**2 +(dy)**2) > 0.00000001:
    x0 = x
    y0 = y
    x = x0 - a * ((z_func(x0+0.0000001, y0)-z_func(x0, y0))/0.0000001)
    y = y0 - a * ((z_func(x0, y0+0.0000001)-z_func(x0, y0))/0.0000001)
    dx = x - x0
    dy = y - y0
    df = z_func(x, y) - fP
    fP = z_func(x, y)
    i = i + 1
    lX.append(x0)
    lY.append(y0)
    lZ.append(fP)
end_time = time.time()
elapsed_time = end_time - start_time

print('Время нахождения минимума: ', elapsed_time)
print('Точка минимума функции: (' + str(x) + ',' + str(y) + ')')
print('Значение функции в точке: ' + str(fP))
print('Значение градиента функции в точке: ' + str(((z_func(x+0.0000001, y)-z_func(x, y))/0.0000001))+' '+str((z_func(x0, y0+0.0000001)-z_func(x0, y0))/0.0000001))
print('Количество итераций: ' + str(i))

x = np.arange(-2.0,2.0,0.01)
y = np.arange(-2.0,2.0,0.01)
X,Y = np.meshgrid(x, y) 
Z = z_func(X, Y) 
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

surf = ax.plot_surface(X, Y, Z, rstride=1, cmap=cm.RdBu)
ax.plot(lX, lY, lZ, color='g')
plt.show()





