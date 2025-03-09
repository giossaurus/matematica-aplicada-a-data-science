#Exercício 2 - Calculando cos(75º) como cos(45º + 30º) usando as fórmulas de soma e diferença
import numpy as np
import matplotlib.pyplot as plt

# Convertendo graus para radianos
deg_to_rad = np.pi / 180

# 1. Cálculo direto de cos(75°)
cos_75_direct = np.cos(75 * deg_to_rad)

# 2. Cálculo usando a fórmula de soma cos(α+β) = cos(α)cos(β) - sin(α)sin(β)
cos_45 = np.cos(45 * deg_to_rad)
sin_45 = np.sin(45 * deg_to_rad)
cos_30 = np.cos(30 * deg_to_rad)
sin_30 = np.sin(30 * deg_to_rad)

cos_75_formula = cos_45 * cos_30 - sin_45 * sin_30

# Exibindo os resultados
print(f"cos(75°) calculado diretamente = {cos_75_direct}")
print(f"cos(75°) calculado por cos(45° + 30°) = {cos_75_formula}")
print(f"Diferença: {abs(cos_75_direct - cos_75_formula)}")

# Gráficos para visualizar as identidades trigonométricas
# Intervalo de ângulos para o gráfico (de 0° a 360°)
angles_deg = np.linspace(0, 360, 300)
angles_rad = angles_deg * deg_to_rad

# Figura com dois subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# 1. Primeiro gráfico: cos(α+β) vs. cos(α)cos(β) - sin(α)sin(β)
# Usando α = θ e β = 30° para ilustrar
alpha_rad = angles_rad
beta_rad = 30 * deg_to_rad

# Calculando as expressões
direct_sum = np.cos(alpha_rad + beta_rad)
formula_sum = np.cos(alpha_rad) * np.cos(beta_rad) - np.sin(alpha_rad) * np.sin(beta_rad)

# Plotando no primeiro gráfico
ax1.plot(angles_deg, direct_sum, label='cos(θ + 30°)', color='blue')
ax1.plot(angles_deg, formula_sum, label='cos(θ)cos(30°) - sin(θ)sin(30°)', 
         linestyle='--', color='red')
ax1.set_xlabel('θ (graus)')
ax1.set_ylabel('Valor')
ax1.set_title('Verificação da Fórmula de Soma de Cossenos')
ax1.legend()
ax1.grid(True)
ax1.axhline(y=0, color='k', linestyle='-', alpha=0.3)
ax1.axvline(x=75, color='green', linestyle='--', label='75°')
ax1.text(75, cos_75_direct, f'cos(75°) = {cos_75_direct:.4f}', 
         bbox=dict(facecolor='white', alpha=0.7))

# 2. Segundo gráfico: calculando cos(θ) diretamente
ax2.plot(angles_deg, np.cos(angles_rad), label='cos(θ)', color='purple')
ax2.axvline(x=75, color='green', linestyle='--', label='75°')
ax2.text(75, cos_75_direct, f'cos(75°) = {cos_75_direct:.4f}', 
         bbox=dict(facecolor='white', alpha=0.7))
ax2.set_xlabel('θ (graus)')
ax2.set_ylabel('Valor')
ax2.set_title('Função Cosseno')
ax2.legend()
ax2.grid(True)
ax2.axhline(y=0, color='k', linestyle='-', alpha=0.3)

plt.tight_layout()
plt.show()