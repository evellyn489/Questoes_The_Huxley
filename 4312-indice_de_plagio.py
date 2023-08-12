def indice_plagio(texto1, texto2):
    contador = 0

    separacao_palavrat1 = texto1.split()
    separacao_palavrat2 = texto2.split()

    for palavra in set(separacao_palavrat1):
        if palavra in separacao_palavrat2:
            contador += 1

    plagio = (contador / (len(separacao_palavrat1) + len(separacao_palavrat2))) * 100

    return (f'{plagio:.1f}')

texto1 = str(input()).lower()
texto2 = str(input()).lower()

print(indice_plagio(texto1, texto2))