idade = int(input())
jogo = str(input())

if not(0 <= idade <= 130):
    print('Idade invalida.')

else:
    if jogo != 'azar' and jogo != 'mmorpg' and jogo != 'moba' and jogo != 'casual':
        print('Jogo invalido.')

    else:
        if (jogo == 'azar' and idade >= 21) or (jogo == 'mmorpg' and idade >= 14) or (jogo == 'moba' and idade >=10) or (jogo == 'casual'):
            print('Pode entrar!')

        else:
            print('Volte daqui há alguns anos.')