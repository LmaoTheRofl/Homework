import math
import numpy as np
from matplotlib import pyplot as plt
from copy import deepcopy

#Длина стола ширина стола
Lx = 2.0
Ly = 2.0 

#Координаты лузы
x0 = 1.5
y0 = 0.8

#Координаты красного шарика
x1 = 0.6
y1 = 0.8

#Координаты зеленого шарика
x2 = 1.1
y2 = 1.1

#Радиус лузы
R = 0.2

#Радиус шариков
r = 0.05

#Масса шариков
m = 0.3 

#Начальная скорость шара
V0 = 2

#Коэффициент трения
mu1 = 0.01
mu2 = 0.05 
mu3 = 0.1
class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def norm(self):
        return math.sqrt(self.x**2 + self.y**2) 
    def distance(self, cord):
        return math.sqrt((self.x - cord.x)**2 + (self.y - cord.y)**2)
    def __add__(self, coordinates):
        return Coordinates(self.x + coordinates.x, self.y + coordinates.y)
    def __sub__(self, coordinates):
        return Coordinates(self.x - coordinates.x, self.y - coordinates.y)
    def __mul__(self, const):
        return Coordinates(const*self.x, const*self.y)
    def __rmul__(self, const):
        return Coordinates(const*self.x, const*self.y)
    def __truediv__(self, const):
        return Coordinates(self.x / const, self.y / const)
    def __lt__(self, coordinates):
        return self.x < coordinates.x or self.y < coordinates.y

class Ball:
    def __init__(self, coordinates : Coordinates, speed : Coordinates, acceleration : Coordinates, m, r):
        self.coordinates = coordinates
        self.setSpeed(speed)
        self.setAcceleration(acceleration)
        self.m = m
        self.r = r
    def setSpeed(self, speed):
        self.speed = deepcopy(speed)
    def getSpeed(self):
        return self.speed
    def setAcceleration(self, acceleration : Coordinates):
        self.acceleration = deepcopy(acceleration)
    def getAcceleration(self):
        return self.acceleration
    
    def iteration(self, dt):
        dv = dt*self.acceleration
        if abs(self.speed.x) < abs(dv.x):
            dv.x = -self.speed.x
        if abs(self.speed.y) < abs(dv.y):
            dv.y = -self.speed.y
        self.coordinates = self.coordinates + dt*self.speed
        self.speed = self.speed + dv

    def isCollision(self, ball):
        return self.coordinates.distance(ball.coordinates) <= self.r + ball.r
    
    def isCollisionWall(self, Lx, Ly):
        def is_collision_side(Lx):
            if self.coordinates.x + self.r >= Lx or self.coordinates.x - self.r <= 0:
                return -1
            else:
                return 1
        def is_collision_end(Ly):
            if self.coordinates.y + self.r >= Ly or self.coordinates.y - self.r <= 0:
                return -1
            else:
                return 1
        self.speed.x = self.speed.x * is_collision_side(Lx)
        self.speed.y = self.speed.y * is_collision_end(Ly)
        self.acceleration.x = self.acceleration.x * is_collision_side(Lx)
        self.acceleration.y = self.acceleration.y * is_collision_end(Ly)

results = {
    mu1 : dict(zip(np.linspace(0, 2*np.pi, 360).tolist(), [-1]*360)),
    mu2 : dict(zip(np.linspace(0, 2*np.pi, 360).tolist(), [-1]*360)),
    mu3 : dict(zip(np.linspace(0, 2*np.pi, 360).tolist(), [-1]*360))
}
dt = 0.001
for mu, result in results.items():
    for i in result.keys():
        RedBall = Ball(Coordinates(x1, y1),Coordinates(V0*math.cos(i), V0*math.sin(i)),Coordinates(-mu*9.80665*math.cos(i), -mu*9.80665*math.sin(i)), m, r)
        GreenBall = Ball(Coordinates(x2, y2), Coordinates(0, 0), Coordinates(0, 0), m, r)
        Hole = Ball(Coordinates(x0, y0), None, None, 0, R)
        for t in np.linspace(0, 10, 10000):
            if RedBall.isCollision(GreenBall):
                d = 0
                x = 0
                if RedBall.speed.x != 0:
                    x = math.atan(RedBall.speed.y / RedBall.speed.x)
                    if RedBall.speed.y > 0 and RedBall.speed.x < 0 or RedBall.speed.y < 0 and RedBall.speed.x < 0:
                        x += math.pi
                    RB = RedBall.coordinates.y - RedBall.speed.y / RedBall.speed.x * RedBall.coordinates.x
                    GB = GreenBall.coordinates.y - RedBall.speed.y / RedBall.speed.x * GreenBall.coordinates.x
                    d = (RB - GB) / math.sqrt((RedBall.speed.y / RedBall.speed.x)**2 + 1)
                else:
                    if RedBall.speed.y > 0:
                        alpha = math.pi / 2
                    else:
                        alpha = -math.pi / 2
                    RB = RedBall.coordinates.x
                    GB = GreenBall.coordinates.x
                    d = RB - GB
                if abs(RB - GB) == 0: 
                    GreenBall.setSpeed(RedBall.getSpeed())
                    GreenBall.setAcceleration(RedBall.getAcceleration())
                else:
                    phi = math.acos(abs(d)/(2*r))
                    if x != math.pi / 2:
                        if (d > 0) == (RedBall.speed.x > 0): 
                            phiRed = x + phi
                            phiGreen = x - (math.pi / 2 - phi)
                        else: 
                            phiRed = x - phi
                            phiGreen = x + (math.pi / 2 - phi)
                    else:
                        if (RB < GB) == (RedBall.coordinates.x < GreenBall.coordinates.x):
                            phiRed = x + phi
                            phiGreen = x - (math.pi / 2 - phi)
                        else:
                            phiRed = x - phi
                            phiGreen = x + (math.pi / 2 - phi)
                    GBSpeedNorm = RedBall.speed.norm() * math.sin(x - phiRed) / math.sin(phiGreen - phiRed)
                    GreenBall.setSpeed(Coordinates(GBSpeedNorm*math.cos(phiGreen), GBSpeedNorm*math.sin(phiGreen)))
                    GreenBall.setAcceleration(Coordinates(-mu*9.80665*math.cos(phiGreen), -mu*9.80665*math.sin(phiGreen)))
                    RBSpeedNorm = RedBall.speed.norm() / math.cos(phiRed) * (math.cos(x) - math.cos(phiGreen)*math.sin(x - phiRed) / math.sin(phiGreen - phiRed))
                    RedBall.setSpeed(Coordinates(RBSpeedNorm*math.cos(phiRed), RBSpeedNorm*math.sin(phiRed)))
                    RedBall.setAcceleration(Coordinates(-mu*9.80665*math.cos(phiRed), -mu*9.80665*math.sin(phiRed)))
            if GreenBall.isCollision(Hole):
                result[i] = m * GreenBall.speed.norm()**2 / 2
                break
            if RedBall.speed.x == 0 and RedBall.speed.y == 0 and GreenBall.speed.x == 0 and GreenBall.speed.y == 0:
                break
            RedBall.isCollisionWall(Lx, Ly)
            GreenBall.isCollisionWall(Lx, Ly)
            RedBall.iteration(dt)
            GreenBall.iteration(dt)
            

color1 = 'white'
color2 = 'black'
color0 = color2

_results = {
    mu1: None,
    mu2: None,
    mu3: None
}
for mu in results.keys():
    arrays = []
    array = {}
    for key, value in results[mu].items():
        if value != -1:
            array.update({key: value})
        else:
            if len(array) != 0:
                arrays.append(array.copy())
                array.clear()
    _results[mu] = arrays

fig = plt.figure(figsize=(15, 10))

ax = fig.add_subplot()
plt.minorticks_on()
plt.xlim((0, 360))
plt.grid(which='major', color='grey')
plt.grid(which='minor', color='grey')
plt.ylabel("Энергия шара $E$ (Дж)", fontsize=20, color=color0)
plt.xlabel("Угол $\\alpha$ (град)", fontsize=20, color=color0)
ax.tick_params(axis='x', colors=color0)
ax.tick_params(axis='y', colors=color0)
colors = {
    mu1: 'r',
    mu2: 'g',
    mu3: 'b'
}
for mu, segments in _results.items():
    lbl = 'mu = ' + str(mu)
    for segment in segments:
        plt.plot([angle * 180 / math.pi for angle in list(segment.keys())], list(segment.values()), color=colors[mu], label=lbl)
        lbl = ''
# Нахождение точек перегиба
dy_dx = np.gradient( list(results[mu2].values()),[angle * 180 / math.pi for angle in list(results[mu2].keys())]) 
d2y_dx2 = np.gradient(dy_dx, [angle * 180 / math.pi for angle in list(results[mu2].keys())])  

inflection_points = []

for i in range(len([angle * 180 / math.pi for angle in list(results[mu2].keys())]) - 1):
    if d2y_dx2[i] * d2y_dx2[i+1] < 0:  
        inflection_points.append(([angle * 180 / math.pi for angle in list(results[mu2].keys())][i],  list(results[mu2].values())[i]))
print("Точки перегиба на графике:")
for point in inflection_points:
    print(f"x={point[0]:.2f}, y={point[1]:.2f}")
plt.legend()
plt.grid(True)
plt.savefig('graph.png')
plt.show()