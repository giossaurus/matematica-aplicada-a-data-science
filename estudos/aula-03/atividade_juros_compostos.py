#Atividade iterativa Juros Compostos
P = 1000  # Capital inicial
r = 0.5  # Taxa de juros
t = np.arange(0, 10, 1)  # Tempo em anos

montante = P * (1 + r) ** t
plt.plot(t, montante, marker="o")
plt.title("Juros Compostos")
plt.xlabel("Tempo (anos)")
plt.ylabel("Montante (R$)")
plt.show()