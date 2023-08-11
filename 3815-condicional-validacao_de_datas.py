dia = int(input())

if dia < 1 or dia > 31:
    print('Dia inexistente')

else:
    mes = int(input())
    if mes < 1 or mes > 12:
        print('Mês inexistente')
    elif dia == 30 and mes == 2:
        print('Esse dia não existe nesse mês')
    elif dia == 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 11 or mes == 2):
        print('Esse dia não existe nesse mês')

    else:
        ano = int(input())

        if not(ano >= 1900 and ano <= 2020):
            print('Ano inexistente')
            
        elif mes == 2:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                if dia > 29:
                    print('Esse dia não existe nesse mês')
                else:
                    print('Data Validada')
            else:
                if dia > 28:
                    print('Esse ano não é bissexto')
                else:
                    print('Data Validada')
                    
        else:
            print('Data Validada')