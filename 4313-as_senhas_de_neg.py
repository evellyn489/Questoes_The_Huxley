tabela = {'0': '6', '1': '7', '2': '9', '3': '8', '4': 'A', '5': '2', '6': 'B', '7': 'F', '8': '1', '9': 'C', 'A': '0', 'B': 'D', 'C': 'E', 'D': '3', 'E': '5', 'F': '4'}

qtd_senhas = int(input())
valido = True

criptografado = '-'
qtd_caracteres = 0

for i in range(qtd_senhas):
    senha = input()

    for letra in senha:
        if not letra.isupper() and not letra.isnumeric():
            valido = False
        else:
            if letra in tabela.keys():
                criptografado += tabela[letra]
            else:
                criptografado += letra
        qtd_caracteres += 1
    
    if i != qtd_senhas - 1:
        criptografado += '-'
    

if valido == False:
    print('Alguma senha eh invalida!')
else:
    print(criptografado, qtd_caracteres)