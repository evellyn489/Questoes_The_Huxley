linhas_matrizA, cl_matrizAeB, colunas_matrizB = [int(x) for x in input().split()] 

if linhas_matrizA == colunas_matrizB:

    matrizA = []
    matrizB = []
    nova_matriz = []

    for _ in range(linhas_matrizA):
        linhaA = [int(x) for x in input().split()]
        matrizA.append(linhaA)
    
    for _ in range(cl_matrizAeB):
        linhaB = [int(x) for x in input().split()]
        matrizB.append(linhaB)

    for _ in range(linhas_matrizA):
        nova_matriz.append([0] * colunas_matrizB)

    for i in range(linhas_matrizA):
        for j in range(colunas_matrizB):
            for k in range(cl_matrizAeB):
                nova_matriz[i][j] += matrizA[i][k] * matrizB[k][j]

    for linha in nova_matriz:
        nova_linha = []
        for elemento in linha:
            nova_linha.append(elemento)
        print(*nova_linha)