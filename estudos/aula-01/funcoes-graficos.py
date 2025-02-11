import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = -x + 2

plt.plot(x, y, label="f(x) = -x +2")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()
