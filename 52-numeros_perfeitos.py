nummeros_menores = 1

numero = int(input())

while nummeros_menores < numero:
    divisores = 0
    
    for i in range(1, nummeros_menores + 1):
        if nummeros_menores % i == 0:
            divisores += i

    dobro = nummeros_menores * 2

    if dobro == divisores:
        print(nummeros_menores)

    nummeros_menores += 1