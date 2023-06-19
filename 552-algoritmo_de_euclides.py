def algoritmo_euclides(n1, n2):
    while n2 != 0:
        resto = n1%n2
        n1 = n2
        n2 = resto
    return n1

entradas = int(input())

for i in range(entradas):
    n1, n2 = [int(x) for x in input().split()]
    print(f'MDC({n1},{n2}) = {algoritmo_euclides(n1, n2)}')