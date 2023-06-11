import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
def model(y, t, b, w0):
    theta, omega = y
    dydt = [omega, -b*(1-theta**2)*omega - w0*theta]
    return dydt
b = -1
w0 = 1
y0 = [0.01, 0]
t = np.linspace(0, 50, 1000)
sol = odeint(model, y0, t, args=(b, w0))
plt.plot(t, sol[:, 0])
plt.xlabel('Время, с')
plt.ylabel('Угол, рад')
plt.title('График зависимости угла поворота маятника от времени')
plt.grid(True)
plt.show()
def model2(y, t, b, w0, a, w):
    theta, omega = y
    dydt = [omega, a*np.sin(w*t) - b*(1-theta**2)*omega - w0*theta]
    return dydt
a_values = np.linspace(0, 2, 5)
w_values = np.linspace(0, 2, 100)
amplitude = []
for a in a_values:
    amplitude_w = []
    for w in w_values:
        sol = odeint(model2, y0, t, args=(b, w0, a, w))
        amplitude_w.append(max(sol[:, 0]))
    amplitude.append(amplitude_w)
for i in range(len(a_values)):
    plt.plot(w_values, amplitude[i], label='a='+str(round(a_values[i],2)))
plt.xlabel('ω')
plt.ylabel('Амплитуда')
plt.title('График зависимости амплитуды установившихся колебаний от частоты внешнего воздействия')
plt.legend()
plt.grid(True)
plt.show()
def find_frequency_range(amplitude, w_values):
    max_amp = max(amplitude)
    min_amp = min(amplitude)
    if max_amp != min_amp:
        threshold = (max_amp + min_amp) / 2
        above_threshold = [i for i, amp in enumerate(amplitude) if amp > threshold]
        if above_threshold:
            return w_values[above_threshold[0]], w_values[above_threshold[-1]]
    return None, None
a_values = np.linspace(0, 2, 20)
frequency_range = []
for a in a_values:
    amplitude_w = []
    for w in w_values:
        sol = odeint(model2, y0, t, args=(b, w0, a, w))
        amplitude_w.append(max(sol[:, 0]))
    w_min, w_max = find_frequency_range(amplitude_w, w_values)
    if w_min is not None and w_max is not None:
        frequency_range.append(w_max - w_min)
    else:
        frequency_range.append(0)
plt.plot(a_values, frequency_range)
plt.xlabel('a')
plt.ylabel('Диапазон частот')
plt.title('График зависимости ширины диапазона частот, при которых колебания происходят только на частоте внешнего воздействия, от амплитуды внешнего воздействия')
plt.grid(True)
plt.show()
