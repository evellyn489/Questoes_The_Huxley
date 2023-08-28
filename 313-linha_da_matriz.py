linha = int(input())
operacao = input()

matriz = None
for i in range(12):
    elementos = [int(x) for x in input().split()]

    if i == linha:
        matriz = elementos

soma = sum(matriz)
if operacao == 'S':
    print(f'{soma:.1f}')
elif operacao == 'M':
    media = soma / len(matriz)
    print(f'{media:.1f}')

