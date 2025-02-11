import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 3, 100)
y = 4*x**2 - 6*x + 1

plt.plot(x, y, label="f(x) = 4x**2 -6x +1")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()