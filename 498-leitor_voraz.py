totalPaginas = int(input())

lidas = []

for i in range(7):
    pagina = int(input())
    lidas.append(pagina)

count = 0
for p in range(7):
    try:
        if lidas[p+1] - lidas[p] > count:
            count = lidas[p+1] - lidas[p]
    except IndexError:
        if lidas[p] - lidas[p-1] > count:
            count = lidas[p] - lidas[p-1]

print(max(lidas))
print(count)