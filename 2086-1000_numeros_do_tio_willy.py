while True:
    try:
        lista = []
        for i in range(1000):
            numero = int(input())
            if numero == - 1:
                break
            lista.append(numero)
        final = int(input())

        vezes = lista.count(final)
        print(f'{final} appeared {vezes} times')
    except EOFError:
        break