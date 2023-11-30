soma_nota = 0
for i in range(4):
    nota = float(input())
    if i == 0 or i == 1:
        soma_nota += (nota * 2)
    else:
        soma_nota += (nota * 3)

media_ponderada = soma_nota / 10
print(f'A média ponderada será: {media_ponderada:.2f}')