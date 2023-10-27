instancias = int(input())


for i in range(instancias):
    valido = True

    matriz = [0]*9

    for n in range(9):
        linhas = [int(x) for x in input().split()]
        matriz[n] = linhas 
        
    for e in range(9):
        lista = []
        for elemento in matriz:
            lista.append(elemento[e])
        
        for m in range(9):
            if (m +1) not in lista:
                valido = False
                break
        
        sem_repetir = set(linhas)

        tamanho_linhas = len(linhas)
        linhas_semRepeticao = len(sem_repetir)

        if tamanho_linhas != linhas_semRepeticao:
            valido = False
    

    print(f'Instancia {i+1}')

    if valido == True:
        print('SIM')
    else:
        print('NAO')

    print()