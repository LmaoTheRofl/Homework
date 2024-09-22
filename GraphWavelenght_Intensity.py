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


def readSpecFile(filename):
    with open(filename, 'r') as file:
        wavelength = []
        spec = []
        for line in file:
            string = line.strip().split()
            wavelength.append(string[0])
            spec.append(string[1])
        return wavelength, spec


def parseToFloat(arr):
    arr = [float(num) for num in arr]
    return arr


def normalize(df):
    df['z'] = (df['z'] - df['z'].min()) / (df['z'].max() - df['z'].min())
    return df['z']


excitation, wavelength, intensity = readfile('Markov_Edward_in_DCM.txt')
_, _, intensity1 = readfile('CH2Cl2.txt')
wavelength1, spec = readSpecFile('DCM_Spec.txt')

array = []
for n in wavelength:
    for _ in range(len(excitation)):
        array.append(n)
excitation = excitation * len(wavelength)
wavelength = array

excitation = parseToFloat(excitation)
wavelength = parseToFloat(wavelength)
intensity = parseToFloat(intensity)

intensity1 = parseToFloat(intensity1)

wavelength1 = parseToFloat(wavelength1)
spec = parseToFloat(spec)

for i in range(len(intensity)):
    intensity[i] -= intensity1[i]
    #intensity[i] = intensity1[i] - intensity[i]

df = pd.DataFrame({'x': excitation, 'y': wavelength, 'z': intensity})

String = '292/402.0'.split('/')
A, B = float(String[0]), float(String[1])

df1 = df[df['y'] == B]
#df1 = df1[df1['x']<=340]
df1['z'] = normalize(df1)

df2 = df[df['x'] == A]
#df2 = df2[(df2['y'] >= 313) & (df2['y'] <= 430)]
df2['z'] = normalize(df2)

fig, ax = plt.subplots()

ax.plot(wavelength1, spec, color='green')
ax.legend(['Поглощение'], loc='upper left')
ax.set_xlabel('Длина волны (нм)', fontsize=12)
ax.set_ylabel('Поглощение (абс)', fontsize=12)

ax2 = ax.twinx()
ax2.plot(df1.x, df1.z, 'steelblue')
ax2.plot(df2.y, df2.z, 'red')
ax2.legend(['Возбуждение', 'Эмиссия'], loc='upper right')
ax2.set_ylabel('Интенсивность (отн)', fontsize=12)

# ax.set_title('График пика $(CH_3OH)$')
ax.set_title('График пика $(CH2Cl2)$')
plt.show()
