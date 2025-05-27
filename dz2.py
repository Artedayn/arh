import numpy as np
import matplotlib.pyplot as plt

def priority_encoder(X1, X2, X3, X4):
    if X1:
        return (1, 1, 0)  # a1=1, a2=0, EO=0
    elif X2:
        return (1, 0, 0)  # a1=1, a2=1, EO=0
    elif X3:
        return (0, 1, 0)  # a1=0, a2=1, EO=0
    elif X4:
        return (0, 0, 0)  # a1=0, a2=0, EO=0
    else:
        return (0, 0, 1)  # EO=1 when no input is active

# Генерация всех возможных входных комбинаций
inputs = np.array([[X1, X2, X3, X4] for X1 in [0, 1] for X2 in [0, 1] for X3 in [0, 1] for X4 in [0, 1]])
outputs = np.array([priority_encoder(*inp) for inp in inputs])

# Вывод таблицы истинности
print("X1 X2 X3 X4 | a1 a2 EO")
print("-------------------")
for inp, out in zip(inputs, outputs):
    print(" ".join(map(str, inp)), "|", " ".join(map(str, out)))

# Визуализация
fig, ax = plt.subplots(4, 1, figsize=(8, 6))
time = np.arange(len(inputs))
labels = ['X1', 'X2', 'X3', 'X4', 'a1', 'a2', 'EO']

for i in range(4):
    ax[i].step(time, inputs[:, i], where='post', label=labels[i])
    ax[i].legend()
    ax[i].set_ylim(-0.5, 1.5)

fig, ax = plt.subplots(3, 1, figsize=(8, 4))
for i in range(3):
    ax[i].step(time, outputs[:, i], where='post', label=labels[i+4], color='r')
    ax[i].legend()
    ax[i].set_ylim(-0.5, 1.5)

plt.show()
