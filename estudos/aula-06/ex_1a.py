#Exercício 1 - Verificando a identidade de sinˆ2(45º)+ cosˆ2(45º)=1
import numpy as np
import matplotlib.pyplot as plt

# Intervalo de ângulos
theta = np.linspace(0, 2*np.pi, 300)

# Calcula sinˆ2(45º) e cosˆ2(45º)
sin_45_squared = np.sin(np.pi/4)**2
cos_45_squared = np.cos(np.pi/4)**2
identity_sum = sin_45_squared + cos_45_squared

print(f"sinˆ2(45º) + cosˆ2(45º) = {identity_sum}")

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