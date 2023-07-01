def contagem_regressiva(n):
    if n < 2:
        print(n)
        print('Decolar!')
    else:
        print(n)
        n = contagem_regressiva(n - 1)
