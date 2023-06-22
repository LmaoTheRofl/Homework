import matplotlib.pyplot as plt

In = open('input.txt', 'r')
x = float(In.readline())
h = float(In.readline())
In.close()

def ydev(x, y):
    return ((1/(x**2 + x + 1)) - (y/(x+0.5)))

xn = 0
yn = 1
xdots = []
ydots = []
xdots.append(xn)
ydots.append(yn)
def runge(xn, yn, h):
    k1 = ydev(xn, yn)
    k2 = ydev(xn + h/2, yn + k1*h/2)
    k3 = ydev(xn + h/2, yn + k2*h/2)
    k4 = ydev(xn + h, yn + k3*h)
    return yn + h*(k1 + 2 * k2 + 2 * k3 + k4)/6
while (xn < x):
    yn = runge(xn, yn, h)
    xn = xn + h
    ydots.append(yn)
    xdots.append(xn)
plt.plot(xdots, ydots, label='h=' + str(h))
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
xlen = len(xdots)
Out = open('output.txt', 'w+')
Out.write("Approximate solution with a step h" + '\n')
Out.write("x" + '\t' + "|" + '\t' + "y" + '\n')
Out.write("--------------------------" + '\n')
for i in range (xlen):
    Out.write(str(xdots[i]) + '\t' + "|" + '\t' + str(ydots[i]) + '\n')

h = h/10
xn = 0
yn = 1
xdots2 = []
ydots2 = []
xdots2.append(xn)
ydots2.append(yn)
def runge(xn, yn, h):
    k1 = ydev(xn, yn)
    k2 = ydev(xn + h/2, yn + k1*h/2)
    k3 = ydev(xn + h/2, yn + k2*h/2)
    k4 = ydev(xn + h, yn + k3*h)
    return yn + h*(k1 + 2 * k2 + 2 * k3 + k4)/6
while (xn < x):
    yn = runge(xn, yn, h)
    xn = round(xn + h, 4)
    ydots2.append(yn)
    xdots2.append(xn)
plt.plot(xdots2, ydots2, label='h=' + str(h))
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
xlen = len(xdots2)
Out.write("Approximate solution with a step h/10" + '\n')
Out.write("x" + '\t' + "|" + '\t' + "y" + '\n')
Out.write("--------------------------" + '\n')
for i in range (xlen):
    Out.write(str(xdots2[i]) + '\t' + "|" + '\t' + str(ydots2[i]) + '\n')
Out.close()