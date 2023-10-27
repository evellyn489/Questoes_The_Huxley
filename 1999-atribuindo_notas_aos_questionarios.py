len_gabarito = int(input())

acertos = 0
valido = True

while True:
    gabarito = input().split()

    if len_gabarito != len(gabarito):
        print('Gabarito de tamanho errado. Entre com o novo gabarito:')
    else:
        break

while True:
    resposta = input().split()

    if resposta[0] == 'sair':
        break

    elif len(resposta) != len_gabarito:
        print('Tamanho da resposta diferente do tamanho do gabarito.')
        valido = False

    else:
        resposta_coreta = 0
        for i in range(len_gabarito):
            if resposta[i] == gabarito[i]:
                resposta_coreta += 1
        
        acertos += resposta_coreta
        valido = True

porcentagem = (acertos/len_gabarito)*100

if valido == True:
    print(f'Percentual de acertos: {porcentagem:.1f}')