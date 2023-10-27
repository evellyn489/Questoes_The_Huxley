apostadores = {}
ganhadores = {}

while True:
    nomes_e_apostas = input().split()
    nomes = nomes_e_apostas[0]

    if nomes == 'FIM':
        break

    apostas = [int(x) for x in nomes_e_apostas[1:]]

    apostadores[nomes] = apostas

sorteio = [int(x) for x in input().split('-')]

for chave, valor in apostadores.items():
    acertos = 0
    for item in valor:
        if item in sorteio:
            acertos += 1
    ganhadores[chave] = acertos

ordem_alfabetica = dict(sorted(ganhadores.items(), key=lambda item:item[0]))
ordem_crescente = dict(sorted(ordem_alfabetica.items(), key=lambda item:item[1]))

for key, value in ordem_crescente.items():
    print(key, '+'*value)