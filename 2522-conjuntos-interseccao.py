conjuntoA = {int(x) for x in input().split()}
conjuntoB = {int(x) for x in input().split()}

interseccao = []

for item in conjuntoA:
    if item in conjuntoB:
        interseccao.append(item)

print(*interseccao)


