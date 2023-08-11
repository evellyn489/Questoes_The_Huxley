dia = int(input())

if not(dia >=1 and dia <=31):
    print('Dia inexistente')

mes = int(input())
if not(mes >= 1 and mes<=12):
    print('Mês inexistente')

ano = int(input())

if not(ano >= 1900 and ano <= 2020):
    print('Ano inexistente')