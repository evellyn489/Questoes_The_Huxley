arvores, madeira = [int(x) for x in input().split()]
alturas = [int(x) for x in input().split()]

sem_repeticao = set(alturas)

todos_metros = []
valores_arvores = []

for item in sem_repeticao:
    metros = 0
    for valor in alturas:
        resultado = (valor - item)
        
        if resultado < 0:
            resultado = 0

        metros += resultado

    todos_metros.append(metros)
    valores_arvores.append(item)

comparar = 0
for chave, valor in enumerate(todos_metros):
    if valor == madeira:
        index = chave
        break
    elif valor > madeira:
        if comparar < valor:
            index = chave

valor_serra = valores_arvores[index]
print(valor_serra)