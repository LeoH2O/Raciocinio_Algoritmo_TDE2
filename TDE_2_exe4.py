# Ler 6 valores inteiros, armazenar em um vetor e mostrar na tela os valores invertidos

vetor = []
for x in range(0, 6):
    valor = int(input("Digite um valor: "))
    vetor.append(valor)
rev = list(reversed(vetor))
print(rev)
