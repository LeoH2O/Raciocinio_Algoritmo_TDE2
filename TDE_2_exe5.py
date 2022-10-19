# Ler um vetor de 10 posições e verificar se existem valores iguais e os escreva na tela

vetor = [10, 10, 2, 2, 3, 5, 6, 7, 7, 10]
dup = []

for x in vetor:
    if vetor.count(x) > 1:
        dup.append(x)

print("Números repetidos: ", set(dup))
