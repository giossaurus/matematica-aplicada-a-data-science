# Exercicio 2 - f(x) = 5 * 2**x
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4, 100)

y = 5 * (2 ** x)

plt.plot(x, y, label='f(x) = 5 * 2^x')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.title("Gráfico da função exponencial: f(x) = 5 * 2^x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

plt.show()