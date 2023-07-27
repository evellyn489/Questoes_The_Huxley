idade = int(input())
prova1 = float(input())
prova2 = float(input())
rep = float(input())

media_aritmetica = (prova1 + prova2)/2
if idade>= 18:
    media_final = (media_aritmetica * 6 + rep*3)/8
else:
    soma_notas = 0
    if prova1 < 7 or prova2 < 7:
        if prova1 >= prova2:
            soma_notas += prova1
        elif prova2 > prova1:
            soma_notas += prova2
        if rep > prova1 and rep > prova2:
            soma_notas += rep
        else:
            soma_notas = prova1 + prova2
        media_final = soma_notas/2
    else:
        media_final = media_aritmetica

if media_final >= 5.5 and prova1 >4 and prova2 > 4 and rep >4:
    print('Aprovado')
else:
    print('Reprovado')
