temperatura = float(input())
resposta = str(input())

if resposta != 'S' and resposta != 'N':
    print('Erro')

if temperatura >= 37 and resposta == 'S':
    print('Exames Especiais')
elif temperatura >=37 and resposta == 'N':
    print('Exames Basicos')
elif temperatura <= 37 and resposta == 'N':
    print('Liberado')
elif temperatura < 37 and resposta == 'S':
    print('Exames Basicos')
