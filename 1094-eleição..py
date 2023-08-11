candidatoA = 0
candidatoB = 0
candidatoC = 0
branco = 0
nulo = 0

while True:
    secao = int(input())

    if secao == 0:
        break
    candidatoA += int(input())
    candidatoB += int(input())
    candidatoC += int(input())

    branco += int(input())
    nulo += int(input())

votosValidos = candidatoA + candidatoB + candidatoC
votosInvalidos = branco + nulo
votosTotais = votosValidos + votosInvalidos


print(f'Numero de votantes: {votosTotais}')
print(f'Total A: {candidatoA}')
print(f'Total B: {candidatoB}')
print(f'Total C: {candidatoC}')
print(f'Brancos: {branco}')
print(f'Nulos: {nulo}')
print(f'Validos: {votosValidos}')



if candidatoA > candidatoB and candidatoA > candidatoC:
    vencedor = candidatoA
    print('Candidato mais votado: A')

elif candidatoB > candidatoA and candidatoB > candidatoC:
    vencedor = candidatoB
    print('Candidato mais votado: B')
    
elif candidatoC > candidatoA and candidatoC > candidatoB:
    vencedor = candidatoC
    print('Candidato mais votado: C')

else:
    vencedor = 0
    print('Candidato mais votado: ')

    
if votosInvalidos < votosValidos:
    print('Eleicao valida? True')

else:
    print('Eleicao valida? False')


if vencedor >= (votosValidos*0.5):
    print('Segundo turno? False')
    
else:
    print('Segundo turno? True')