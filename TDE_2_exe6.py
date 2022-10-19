# Ler vetor com 20 números inteiros. Escrever elementos do vetor eliminando repitidos

vetor = []
for x in range(0, 20):
    valor = int(input("Digite um valor: "))
    vetor.append(valor)

print(f'Vetor sem os repetidos: {set(vetor)}')
