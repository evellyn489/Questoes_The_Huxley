valores = [int(x) for x in input().split()]

valores.sort()

meio = len(valores) // 2

if len(valores) % 2 == 0:
    mediana = (valores[meio] + valores[meio-1])/2
    print(f'Mediana = {mediana:.1f}')
else:
    mediana = valores[len(valores) // 2]

    print(f'Mediana = {mediana}')