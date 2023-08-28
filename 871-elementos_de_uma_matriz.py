linhas, colunas = [int(x) for x in input().split()]
 
maior = 0
menor = 0

matriz  = [0] * linhas 

for i in range(linhas):
    matriz[i] = [0] * colunas

for l in range(linhas):
    for c in range(colunas):
        numero = int(input())
        matriz[l][c] = numero

        if numero > 0:
            maior += 1
        elif numero < 0:
            menor += 1

#Organizar a matriz
s = ''
for l in range(linhas):
    s += ''
    for j in range(colunas):
        s += str(matriz[l][j])
        if j < colunas - 1:
            s += ' '
    if l < linhas - 1:
        s += '\n'

print('Matriz formada:')
print(s.strip())

if linhas != colunas:
    print(f'A diagonal principal e secundaria nao pode ser obtida.')
    
else:
    diagonal_secundaria1 = 0
    diagonal_secundaria2 = 0

    for i in range(linhas):
        diagonal_secundaria2 += matriz[i][linhas - 1 - i]
        diagonal_secundaria1 += matriz[i][i]

    print(f'A diagonal principal e secundaria tem valor(es) {diagonal_secundaria2} e {diagonal_secundaria1} respectivamente.')

print(f'A matriz possui {menor} numero(s) menor(es) que zero.')
print(f'A matriz possui {maior} numero(s) maior(es) que zero.')