def binary_search(lista_cpf, cpf):
    left = 0
    right = len(lista_cpf) -1

    while left <= right:
        middle = (left + right)//2

        if lista_cpf[middle] == cpf:
            return middle
        elif lista_cpf[middle] < cpf:
            left = middle + 1
        elif lista_cpf[middle] > cpf:
            right = middle - 1
            
    return -1

qtd_inscritos = int(input())

lista_cpf = [int(input()) for x in range(qtd_inscritos)]
lista_notas = [int(input()) for x in range(qtd_inscritos)]

testes = int(input())

for _ in range(testes):
    pesquisa = int(input())
    index = binary_search(lista_cpf, pesquisa)

    if index != -1:
        nota = lista_notas[index]
        print(nota)
    else:
        print('NAO SE APRESENTOU')