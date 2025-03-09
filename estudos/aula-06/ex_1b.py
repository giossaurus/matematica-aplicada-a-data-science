#Exercício 1 - Verificando a identidade de sinˆ2(60º)+ cosˆ2(60º)=1
import numpy as np
import matplotlib.pyplot as plt

# Intervalo de ângulos
theta = np.linspace(0, 2*np.pi, 300)

# Calcula sinˆ2(60º) e cosˆ2(60º)
sin_60_squared = np.sin(np.pi/4)**2
cos_60_squared = np.cos(np.pi/4)**2
identity_sum = sin_60_squared + cos_60_squared

print(f"sinˆ2(60º) + cosˆ2(60º) = {identity_sum}")

sin_2theta = np.sin(2 * theta)
# Definindo a fórmula do ângulo duplo
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