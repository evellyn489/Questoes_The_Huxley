numero = int(input())

print(numero)
for i in range(numero-1, 0, -1):
    if numero % i == 0:
        print(i)