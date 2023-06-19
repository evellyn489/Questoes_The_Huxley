testes = int(input())

letras = []

def consecutives(nomes):
    letras = []
    for letra in nomes:
        letras.append(letra)

    string = ''
    for i in range(len(letras)):
        if i == len(letras) - 1:
            string += letras[i]
        elif i == 0:
            if letras[i] != letras[i+1]:
                string += letras[i]
            else:
                continue

        elif letras[i] != letras[i+1]:
            string += letras[i]
        elif letras[i] == letras[i-1]:
            continue

    print(string)

for i in range(testes):
    consecutives(input())