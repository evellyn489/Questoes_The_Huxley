array = []

for i in range(5):
    numero = int(input('Digite um numero inteiro:'))
    array.append(numero)

for key, value in enumerate(array):
    print(f'Numero {key + 1}: {value}')