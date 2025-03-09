import numpy as np
import matplotlib.pyplot as plt

# Intervalo de ângulos
theta = np.linspace(0, 2*np.pi, 300)

# Calcula sin(2θ) e 2*sin(θ)*cos(θ)
sin_2theta = np.sin(2*theta)
double_angle = 2 * np.sin(theta) * np.cos(theta)

plt.figure(figsize=(8,5))
plt.plot(theta, sin_2theta, label='sin(2θ)', color='blue')
plt.plot(theta, double_angle, label='2 sin(θ) cos(θ)', linestyle='--', color='red')
plt.xlabel('θ (radianos)')
plt.ylabel('Valor')
plt.title('Verificação da Fórmula do Ângulo Duplo')
plt.legend()
plt.grid(True)
plt.show()
