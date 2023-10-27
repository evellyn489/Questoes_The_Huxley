n = int(input())

notas = 0
for i in range(n):
    notas += float(input())

media = notas/n
print(media)