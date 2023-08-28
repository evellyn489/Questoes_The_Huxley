pedacos = int(input())

organizar = {}
for i in range(pedacos):
    p, letra = input().split()
    posicao = int(p)

    organizar[posicao] = letra

ordenar = dict(sorted(organizar.items()))

palavra = ''
for item in ordenar.values():
    palavra += item

print(palavra)