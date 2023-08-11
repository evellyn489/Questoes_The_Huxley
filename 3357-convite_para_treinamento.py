competidores = int(input())
numeroPontos = int(input())

contador = 0
for i in range(competidores):
    fase1 = int(input())
    fase2 = int(input())

    if fase1 != 0 and fase2 != 0:
        if (fase1 + fase2) >= numeroPontos:
            contador += 1

print(contador)
