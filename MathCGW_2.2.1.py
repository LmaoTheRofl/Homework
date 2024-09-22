import numpy as np
import matplotlib.pyplot as plt

# Векторные линии поля.
x,y = np.meshgrid(np.linspace(-2,2,25),np.linspace(-2,2,25))
devx = 1/(3*np.cbrt(x**2))
devy = 1/(3*np.cbrt(y**2))
plt.streamplot(x,y,devx,devy, density=1)
plt.title('Vector Lines')
plt.grid()


# Линии уровня потенциала.
x,y = np.meshgrid(np.arange(-3,3,0.01),np.arange(-3,3,0.01))
u = np.cbrt(x)+np.cbrt(y)
fig, ax = plt.subplots()
CS = ax.contour(x,y,u)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Oxy projection')
plt.grid()



fig, ax = plt.subplots()
#CS = ax.contour(y,u,x)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Oyz projection')
plt.grid()


fig, ax = plt.subplots()
#CS = ax.contour(x,u,y)
ax.clabel(CS, inline=True, fontsize=10)
ax.set_title('Oxz projection')
plt.grid()
plt.show()