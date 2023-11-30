valores = [int(x) for x in input().split()]

contagem = [0] * len(valores)

for i in range(len(valores)):
    contagem[i] = valores.count(valores[i])

maior_contagem = max(contagem)

for j in range(len(valores)):
    if contagem[j] == maior_contagem:
        print(f'Moda = {valores[j]}')
        break