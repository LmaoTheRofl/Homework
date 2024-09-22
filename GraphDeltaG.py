
import matplotlib.pyplot as plt

# Данные для точек
points = {
    'red': [(1, -2.534768), (2, -5.191047), (3, -5.209596), (4, -3.359152), (5, -5.480373), (6, -15.096360), (7, 7.0562), (8, 2.058940), (9, -16.164306), (10, -12.110456)],
    'blue': [(1, -2.639957), (2, -6.599021), (3, -3.151459), (4, -6.526563), (5, -9.161582), (6, -4.958680), (7, 0.18038), (8, -1.419941), (9, -8.502333), (10, 1.280991)],
    'green': [(1, -5.124976), (2, -5.149581), (3, -0.71704882), (4, -11.453033), (5, -0.382278), (6, -12.085111), (7, -5.182946), (8, -6.204858), (9, 0.499158), (10, -6.541020)]
}

# Создание графика
plt.figure()
plt.xlabel('количество молекул $(H_2O)$')
plt.ylabel('deltaG ккал/моль')
plt.xlim(0, 11)
plt.ylim(-18, 18)
plt.xticks(range(12))  
plt.yticks([i for i in range(-18, 18, 1)]) 
for color, data in points.items():
    x = [point[0] for point in data]
    y = [point[1] for point in data]
    plt.scatter(x, y, color=color)
plt.text(9, 16, "красный - манноза", fontsize=11, bbox=dict(facecolor='red', alpha=0.5))
plt.text(9, 13, "синий - глюкоза", fontsize=11, bbox=dict(facecolor='blue', alpha=0.5))
plt.text(9, 10, "зеленый - рибоза", fontsize=11, bbox=dict(facecolor='green', alpha=0.5))
plt.show()