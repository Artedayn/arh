import numpy as np
import matplotlib.pyplot as plt

tc = 1e-3
h = 1e-6
steps = int(tc / h)

frq1 = 5000
frq2 = 10000
period1 = int(1 / (frq1 * h))
period2 = int(1 / (frq2 * h))

T1 = 1e-5
T2 = 2e-5

A1 = 0.1
A2 = 0.3

Umin1, Umax1 = 1.5, 3.5
Umin2, Umax2 = 2.0, 4.0


Y1 = np.zeros(steps)
Y2 = np.zeros(steps)
U1 = np.zeros(steps)
U2 = np.zeros(steps)
U1_noises = np.zeros(steps)
U2_noises = np.zeros(steps)

for i in range(steps):
    if (i // period1) % 2 == 0:
        Y1[i] = 0.5
    else:
        Y1[i] = 4.5

    if (i // period2) % 2 == 0:
        Y2[i] = 0.5
    else:
        Y2[i] = 4.5

for i in range(1, steps):
    U1[i] = U1[i - 1] + h * (Y1[i] - U1[i - 1]) / T1
    U2[i] = U2[i - 1] + h * (Y2[i] - U2[i - 1]) / T2

    noises1 = np.random.uniform(-A1, A1)
    noises2 = np.random.uniform(-A2, A2)
    U1_noises[i] = U1[i] + noises1
    U2_noises[i] = U2[i] + noises2

Out1 = np.zeros(steps)
Out2 = np.zeros(steps)

for i in range(1, steps):
    if Out1[i - 1] == 0:
        Out1[i] = 0 if U1_noises[i] < Umax1 else 4.5
    else:
        Out1[i] = 4.5 if U1_noises[i] > Umin1 else 0.5

    if Out2[i - 1] == 0:
        Out2[i] = 0 if U2_noises[i] < Umax2 else 4.5
    else:
        Out2[i] = 4.5 if U2_noises[i] > Umin2 else 0.5

plt.figure(figsize=(10, 8))
plt.subplot(2, 1, 1)
plt.plot(np.arange(steps) * h * 1e3, Y1, label='Меандр 5 кГц')
plt.plot(np.arange(steps) * h * 1e3, U1, label='U1 с ёмкостью', linestyle='dashed')
plt.plot(np.arange(steps) * h * 1e3, U1_noises, label='U1 с помехами', linestyle='dotted', color='red')
plt.plot(np.arange(steps) * h * 1e3, Out2, label='Выходной сигнал 10 кГц', linestyle='dashdot', color='purple')
plt.legend()
plt.grid()
plt.ylabel('Напряжение (В)')
plt.title('Генератор импульсов 5 кГц: ёмкостный эффект и помехи')

plt.subplot(2, 1, 2)
plt.plot(np.arange(steps) * h * 1e3, Y2, label='Меандр 10 кГц', color='orange')
plt.plot(np.arange(steps) * h * 1e3, U2, label='U2 с ёмкостью', linestyle='dashed', color='red')
plt.plot(np.arange(steps) * h * 1e3, U2_noises, label='U2 с помехами', linestyle='dotted', color='blue')
plt.plot(np.arange(steps) * h * 1e3, Out2, label='Выходной сигнал 10 кГц', linestyle='dashdot', color='purple')
plt.legend()
plt.grid()
plt.ylabel('Напряжение (В)')
plt.xlabel('Время (мс)')
plt.title('Генератор импульсов 10 кГц: ёмкостный эффект и помехи')

plt.tight_layout()
plt.show()


"""
Вывод
Помехи и ёмкостные эффекты могут значительно искажать цифровые сигналы, что требует использования специальных методов фильтрации и защиты для надежной передачи данных.
"""