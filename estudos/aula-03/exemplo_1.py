#Exemplo 01
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)
y1 = 1000 + (100* x)  # Crescimento
y2 = 1000 * (2 ** x)  # Decaimento

plt.plot(x, y1)
plt.plot(x, y2)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.title("Funções Exponenciais")
plt.show()