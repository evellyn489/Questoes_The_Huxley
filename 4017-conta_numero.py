
primeiro_numero = int(input())

lista_numeros = []

frequencia = 0

for i in range(20):
    numero = int(input())

    if numero == -1:
        break
    else:
        if numero == primeiro_numero:
            frequencia += 1
        if (numero > 0 and not 15 <= numero <= 20):
            lista_numeros.append(numero)

print(f'O número {primeiro_numero} apareceu {frequencia} vez(es)')

qtd_numeros = len(lista_numeros)
soma_numeros = sum(lista_numeros)

if qtd_numeros != 0:
    media = soma_numeros/qtd_numeros

if soma_numeros != 0:
    print(f'A média dos números foi de: {media:.2f}')
else:
    print('Sem valores para calcular a média')