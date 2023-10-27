print('Digite as dimensoes da matriz:')
print('Digite os elementos da matriz:')

linhas, colunas = [int(x) for x in input().split()]

matriz = [0]*linhas 

for i in range(linhas):
    matriz[i] = [0]*colunas

for l in range(linhas):
    linha = [int(x) for x in input().split()]
    for j in range(colunas):
        matriz[l][j] = linha[j]

transposta = [0]*colunas

for i in range(colunas):
    transposta[i] = [0]*linhas

for i in range(linhas):
    for j in range(colunas):
        transposta[j][i] = matriz[i][j]
    
print('Matriz transposta:')

count = 0
for elemento in transposta:
    tamanho_elemento = len(elemento)

    count += 1

    for i in range(tamanho_elemento):
        if i != tamanho_elemento-1:
            print('{:<6}'.format(elemento[i]), end='')
        else:
            if count != colunas:
                print(f'{elemento[i]}     ')
            else:
                print(f'{elemento[i]}')