import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 3, 100)
y = 2*x**2 - 3*x + 1

plt.plot(x, y, label="f(x) = 2x**2 -3x +1")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()