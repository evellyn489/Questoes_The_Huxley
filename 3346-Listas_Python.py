numeros = []
terminou = False

while not terminou:
    entrada = int(input())
    if entrada == -1:
        terminou = True
    else:
        numeros.append(entrada)

media_aritmetica = sum(numeros)/len(numeros)

print('%.2f' %media_aritmetica)