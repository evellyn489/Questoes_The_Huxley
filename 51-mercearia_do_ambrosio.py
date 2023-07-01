codigos = {1: 5.30, 2 : 6.00, 3 : 3.20, 4: 2.50 }

produto = int(input())
quantidade = int(input())

resultado = codigos[produto] * quantidade

if quantidade >= 15 or resultado >= 40:
    total = resultado - (resultado*15)/100
    print('R$ %.2f' %total)
else:
    print('R$ %.2f\n' %resultado)
