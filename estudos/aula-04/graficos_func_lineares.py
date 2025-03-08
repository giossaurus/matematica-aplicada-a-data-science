import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 10, 100)
y1 = np.log2(x)
y2 = np.log10(x)
y3 = np.log(x)

plt.figure(figsize=(8,5))
plt.plot(x, y1, label='log_2(x)')
plt.plot(x, y2, label='log_10(x)')
plt.plot(x, y3, label='ln(x)')
plt.axhline(0, color='black', linewidth=1)
plt.axvline(1, color='black', linestyle='--')
plt.legend()
plt.title('Gráficos de Funções Logarítmicas')
plt.show()