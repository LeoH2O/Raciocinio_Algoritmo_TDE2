# Programa que preenche um vetor com valores inteiros até que o usuário digite um valor negativo
# Imprimir o vetor;
# Quantidade de valores maiores que 5;
# Soma dos valores pares armazenados no vetor;
# Soma dos valores ímpares armazenados no vetor;
# Quantidade total de valores armazenados no vetor.

vetor = []
numero = 0
par = 0
impar = 0
quantidade = 0
quant_cinco = 0
while numero > -1:
    numero = int(input("Digite um valor: "))
    if numero > -1:
        vetor.append(numero)
        quantidade = quantidade + 1
        if numero > 5:
            quant_cinco = quant_cinco + 1
        if numero % 2 == 0:
            par += numero
        else:
            impar += numero

print(vetor)
print("Quantia de valores maiores que 5: ", quant_cinco)
print("Soma dos pares: ", par)
print("Soma dos ímpares: ", impar)
print("Quantidade de valores armazenados: ", quantidade)
