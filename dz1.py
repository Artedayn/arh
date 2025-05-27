import numpy as np
import matplotlib.pyplot as plt

frequencies = [10e3, 5e3, 2e3]
amplitude = 5
duration = 1e-3
sampling_step = 1e-6
t = np.arange(0, duration, sampling_step)

triangle_signal = amplitude * (2 * np.abs(2 * (t * frequencies[0] % 1) - 1))

lower_bound = 2
upper_bound = 4

output_signal = np.zeros_like(triangle_signal)

output_signal[triangle_signal > upper_bound] = amplitude
output_signal[triangle_signal < lower_bound] = 0

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t * 1e3, triangle_signal, label='Треугольный сигнал', color='blue')
plt.axhline(y=lower_bound, color='red', linestyle='--', label='Нижняя граница')
plt.axhline(y=upper_bound, color='green', linestyle='--', label='Верхняя граница')
plt.title('Исходный треугольный сигнал с запрещенной зоной')
plt.xlabel('Время (мс)')
plt.ylabel('Амплитуда')
plt.legend()
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t * 1e3, output_signal, label='Выходной сигнал', color='orange')
plt.title('Выходной сигнал логического каскада')
plt.xlabel('Время (мс)')
plt.ylabel('Амплитуда')
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()