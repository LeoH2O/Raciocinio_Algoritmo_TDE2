# Ler um vetor de 15 posições e o compactar a lista de 0

vetor = [1, 0, 4, 3, 4, 0, 7, 0, 6, 20, 10, 45, 0, 9, 0]
lista = []
for x in vetor:
    if x > 0:
        lista.append(x)
zeros = (len(vetor) - len(lista)) * [0]
lista = lista + zeros
print(lista)
