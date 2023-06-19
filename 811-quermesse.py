count = 0

while True:
    try:
        qtd_ingressos = int(input())
        numeros_ingressos= [int(x) for x in input().split()]

        if qtd_ingressos == 0:
            break

        count += 1

        print(f'Teste {count}')
        for chave, valor in enumerate(numeros_ingressos):
            if chave+1 == valor:
                print(valor)
                print()
                break
    except EOFError:
        break