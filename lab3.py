import numpy as np
import matplotlib.pyplot as plt

def generate_clock_signal(T=20, h=1, duration=200):
    t = np.arange(0, duration, h)
    clock = (t // (T // 2)) % 2  # Генерация меандра
    return t, clock * 5

def generate_sdr_signal(data, T=20, h=1):
    bits = bin(data)[2:].zfill(8)
    t = np.arange(0, len(bits) * T, h)
    signal = np.zeros_like(t)
    for i, bit in enumerate(bits):
        if bit == '1':
            signal[i * T:(i + 1) * T] = 5  # Установка уровня сигнала
    return t, signal

def generate_ddr_signal(data, T=20, h=1):
    bits = bin(data)[2:].zfill(8)
    t = np.arange(0, len(bits) * T // 2, h)
    signal = np.zeros_like(t)
    for i, bit in enumerate(bits):
        if bit == '1':
            signal[i * (T // 2):(i * (T // 2) + T // 4)] = 5  # Фронт
            signal[(i * (T // 2) + T // 4):(i * (T // 2) + T // 2)] = 0  # Спад
    return t, signal

# Задаем параметры
T = 20  # Период 20 мкс
h = 1   # Шаг 1 мкс

data_samples = [0x7A, 0xFF, 0x0F]
labels = ["7A(h)", "FF(h)", "0F(h)"]
colors = ['red', 'red', 'red', 'blue', 'blue', 'blue']

# Генерируем и строим графики
fig, axes = plt.subplots(7, 1, figsize=(10, 14), sharex=True)

# Генераторный сигнал
t_clock, clock_signal = generate_clock_signal(T, h)
axes[0].step(t_clock, clock_signal, where='post', color='green', label="Clock Signal")
axes[0].set_title("Синхросигнал генератора")
axes[0].legend()

# SDR сигналы
for i, data in enumerate(data_samples):
    t_sdr, sdr_signal = generate_sdr_signal(data, T, h)
    axes[i + 1].step(t_sdr, sdr_signal, where='post', color=colors[i], label=f"SDR {labels[i]}")
    axes[i + 1].set_title(f"Сигнал SDR {labels[i]}")
    axes[i + 1].legend()

# DDR сигналы
for i, data in enumerate(data_samples):
    t_ddr, ddr_signal = generate_ddr_signal(data, T, h)
    axes[i + 4].step(t_ddr, ddr_signal, where='post', color=colors[i + 3], label=f"DDR {labels[i]}")
    axes[i + 4].set_title(f"Сигнал DDR {labels[i]}")
    axes[i + 4].legend()

# Выводим графики
plt.xlabel("Время (мкс)")
plt.tight_layout()
plt.show()