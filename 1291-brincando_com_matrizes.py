matriz = []
maiores = []

soma = 0
delta = 0
sum_diagonalPrincipal = 0

for i in range(3):
    linha = [0] * 3

    for j in range(3):
        numero = int(input())
        linha[j] = numero

    matriz.append(linha)
    sum_diagonalPrincipal += matriz[i][i]

for item in matriz:
    soma += sum(item)
    maior = max(item)

    maiores.append(maior)

maximo = max(maiores)

if maximo > 0:
    delta = 1
elif maximo == 0:
    delta == 0
else:
    delta = -1

media = soma/9

print(f'{media:.2f} {maximo} {delta} {sum_diagonalPrincipal}')
