numero = [int(x) for x in input().split()]

qtd_numero = 0
for num in numero:
    if num == numero[9]:
        qtd_numero += 1

print(f'O numero {numero[9]} apareceu {qtd_numero} vezes')