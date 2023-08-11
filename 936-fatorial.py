numero = int(input('Digite um número inteiro:\n'))

fat = 1
for i in range(1, numero+1):
    fat *=i

print(f'Fatorial: {fat}' )
