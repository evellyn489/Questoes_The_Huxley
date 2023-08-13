total_comida = 0
dentro = {}

comandos = int(input())

for i in range(comandos):
    entrada = input().split(':')

    resposta = entrada[0]
    anao = entrada[1]

    if resposta == 'ENTROU':
        qtd_comida = int(input())
        if anao in dentro:
            print('Anao ja estava em casa.')
        else:
            dentro[anao] = qtd_comida

            print(f'{entrada[1]} entrou e gostaria de {qtd_comida}g de comida.')
    elif resposta == 'SAIU':
        if anao not in dentro:
            print(f'{anao} nao estava na casa.')
        else:
            dentro.pop(anao)
            print(f'{anao} saiu de casa.')


print()
if len(dentro) == 7:
    print('teoria da branca de neve: porque so ter um se eu posso ter sete?')
else:
    print(f'Estao na casa {len(dentro)} anoes:')

for key, value in dentro.items():
    print(key)

    total_comida += value

print(total_comida)