string = input()

contador = 0
for letra in string:
    try:
        numero = int(letra)
        contador += 1
    except:
        continue

print(contador)