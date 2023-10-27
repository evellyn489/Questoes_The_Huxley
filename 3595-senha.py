password = input()

valido = True
for elemento in password:
    if int(elemento) == 0:
        print('Nao pode')
        valido = False
        break
if valido:
    print('Pode')