qtd_personagens = int(input())

informações = {}
todas_informacoes = []

for i in range(qtd_personagens):
    informações['Nome'] = input()
    informações['ID'] = int(input())
    informações['Level'] = int(input())
    informações['Vida'] = int(input())
    informações['Ataque'] = int(input())
    informações['Defesa'] = int(input())

    todas_informacoes.append(informações.copy())

for dicionario in todas_informacoes:
    for c, v in dicionario.items():
        print(f'{c}: {v}')