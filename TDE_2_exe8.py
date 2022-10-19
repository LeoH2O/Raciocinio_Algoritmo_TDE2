# Dois vetores de 10 posições e inserir em um vetor;
# Vetor 1 nas posições pares;
# Vetor 2 nas posições ímpares.

vetor_1 = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
vetor_2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
unir = []

for x, y in zip(vetor_1, vetor_2):
    unir.append(x)
    unir.append(y)

print(unir)
