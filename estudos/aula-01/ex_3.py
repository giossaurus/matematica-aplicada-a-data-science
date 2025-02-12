import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 3, 100)

y = 25*x - 14

plt.plot(x, y, label="f(x) = 25x - 14")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.show()