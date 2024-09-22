from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def readfile(filename):
    with open(filename, 'r') as file:
        excitation = file.readline().strip().split()
        wavelength = []
        intensity = []
        for line in file:
            row = line.strip().split()
            wavelength.append(row[0])
            row = row[1:]
            for n in row:
                intensity.append(n)
    return excitation, wavelength, intensity


def parseToFloat(arr):
    arr = [float(num) for num in arr]
    return arr

excitation, wavelength, intensity = readfile('CH2Cl2.txt')
#excitation1, wavelength1, intensity1 = readfile('Markov_Edward_in_CLEAR_METANOL.txt')
unique_excitation = excitation

array = []
for n in wavelength:
    for _ in range(len(excitation)):
        array.append(n)
excitation = excitation * len(wavelength)
wavelength = array

excitation = parseToFloat(excitation)
wavelength = parseToFloat(wavelength)
intensity = parseToFloat(intensity)
unique_excitation = parseToFloat(unique_excitation)
#intensity1 = parseToFloat(intensity1)

#for i in range(len(intensity)):
    #intensity[i] -= intensity1[i] #для дихлорметана
    #intensity[i] = intensity1[i] - intensity[i] #для метанола
df = pd.DataFrame({'x': excitation, 'y': wavelength, 'z': intensity})

fig = plt.figure()
ax = plt.axes(projection='3d')

for ex in unique_excitation:
    df1 = df[df['x'] == ex]
    ax.plot(df1.x, df1.y, df1.z, 'steelblue')

ax.set_xlabel('Возбуждение (нм)', fontsize=12)
ax.set_ylabel('эмиссия (нм)', fontsize=12)
ax.set_zlabel('Интенсивность (отн)', fontsize=12)
#ax.set_title('Полный спектр люминисценции $()$')
ax.set_title('Полный спектр люминисценции $(CH_2Cl_2)$')
plt.show()