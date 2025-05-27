import numpy as np
import matplotlib.pyplot as plt

def generate_signals(time_steps):
    X1 = np.tile([0, 1], time_steps // 2)
    X2 = np.tile([0, 0, 1, 1], time_steps // 4)
    X3 = np.tile([0, 0, 0, 0, 1, 1, 1, 1], time_steps // 8)
    X4 = np.tile([0]*8 + [1]*8, time_steps // 16)
    A1 = np.tile([0, 1], time_steps // 2)
    A2 = np.tile([0, 0, 1, 1], time_steps // 4)
    return X1, X2, X3, X4, A1, A2

def decoder(a1, a2):
    D1 = int(not a1 and not a2)
    D2 = int(not a1 and a2)
    D3 = int(a1 and not a2)
    D4 = int(a1 and a2)
    return D1, D2, D3, D4

def multiplexer(x1, x2, x3, x4, a1, a2):
    D1, D2, D3, D4 = decoder(a1, a2)
    return (x1 and D1) or (x2 and D2) or (x3 and D3) or (x4 and D4)

h = 1e-6
time_steps = 16
time = np.arange(0, time_steps * h, h)

X1, X2, X3, X4, A1, A2 = generate_signals(time_steps)
F = [multiplexer(X1[i], X2[i], X3[i], X4[i], A1[i], A2[i]) for i in range(time_steps)]

plt.figure(figsize=(10, 6))
plt.subplot(6, 1, 1)
plt.step(time, X1, where='post', label='X1')
plt.legend()
plt.subplot(6, 1, 2)
plt.step(time, X2, where='post', label='X2')
plt.legend()
plt.subplot(6, 1, 3)
plt.step(time, X3, where='post', label='X3')
plt.legend()
plt.subplot(6, 1, 4)
plt.step(time, X4, where='post', label='X4')
plt.legend()
plt.subplot(6, 1, 5)
plt.step(time, A1, where='post', label='A1')
plt.legend()
plt.subplot(6, 1, 6)
plt.step(time, F, where='post', label='F', color='red')
plt.legend()
plt.xlabel("Time (s)")
plt.show()
