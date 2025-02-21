#Exercicio 1 - f(x) = 8 * 3**x
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 100)
y = 8 * (3 ** x)

plt.plot(x, y)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

plt.title("Gráfico da função exponencial: f(x) = 8 * 3^x")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()

plt.show()