pessoas = 0

todas_idades = []
contador = 0

while True:
    idade = int(input())
    if idade == -1:
        break
    sexo, cabelo, olhos = [x for x in input().split()]
    todas_idades.append(idade)

    if (sexo, cabelo, olhos) == ('f', 'l', 'v') and 18<=idade<=35:
        contador += 1

    pessoas += 1

porcentagem = float((contador * 100)/pessoas)

print(f'Mais velho: {max(todas_idades)}')
print(f'Mulheres com olhos verdes, loiras com 18 a 35 anos: {porcentagem:.2f}%')