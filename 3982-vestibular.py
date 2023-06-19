import time

start_time = time.time()

gabarito = input().split()
dicionario = {}
participante = 0

while True:
    count = 0

    nome_respostas = input().split()

    if nome_respostas == ['*']:
        break
    for i in range(len(gabarito)):
        if nome_respostas[i+1] == gabarito[i]:
            count += 1

    dicionario[nome_respostas[0]] = count
    if count > 5:
        participante += 1

print('Participante Nota')

for chave, valor in sorted(dicionario.items()):
    print(chave, valor)

print(f'Melhor pontuacao: {max(dicionario.values())}')

for key, value in sorted(dicionario.items()):
    if value == max(dicionario.values()):
        print(key)

print(f'Pior pontuacao: {min(dicionario.values())}')

for key, value in sorted(dicionario.items()):
    if value == min(dicionario.values()):
        print(key)

percentual = participante * 10

print(f'Percentual de participantes com mais da metade de questoes certas: {percentual:.1f}%')


print()

end_time = time.time()
total_time = end_time - start_time
print("Tempo total de execução: ", total_time)