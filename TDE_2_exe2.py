# Programa que preenche um vetor de 50 posições com valores aleatórios entre 0 a 20
# A soma dos valores armazenados no vetor;
# O número de ocorrências do valor 9;
# O maior valor armazenado no vetor;
# O menor valor armazenado no vetor.
import random
nine = 0
maior = 0
menor = 0
vetor = []
num = int(random.uniform(1, 21))
for x in range(0, 51):
    num = int(random.uniform(0, 21))
    vetor.append(num)
    if num == 9:
        nine = nine + 1
    if x == 0:
        maior = menor = vetor[x]
    else:
        if vetor[x] > maior:
            maior = vetor[x]
        if vetor[x] <= menor:
            menor = vetor[x]

print(vetor)
print("O número de ocorrências do 9: ", nine)
print("Maior valor armazenado: ", maior)
print("Menor valor armazenado: ", menor)