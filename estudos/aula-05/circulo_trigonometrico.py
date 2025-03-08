import numpy as np
import matplotlib.pyplot as plt

# Cria os dados do círculo unitário
theta = np.linspace(0, 2*np.pi, 300)
x = np.cos(theta)
y = np.sin(theta)

plt.figure(figsize=(6,6))
plt.plot(x, y, label='Círculo Unitário')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.scatter([1, 0, -1, 0], [0, 1, 0, -1], color='red')  # pontos chave: 0, 90, 180, 270°
plt.title("Círculo Trigonométrico")
plt.xlabel("Cos(θ)")
plt.ylabel("Sin(θ)")
plt.legend()
plt.grid(True)
plt.show()