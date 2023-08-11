termos = int(input())

s = 0
qtdTermos = 0

if termos == 0:
    print(f'{0:.5f}')

elif 1 <= termos < 5:
    for i in range(1, termos+1, 4):
        s += 1/(i)**3
        qtdTermos += 1

        if qtdTermos < termos:
            s -= 1/(i+2)**3
            qtdTermos += 1
        pi = (s*32)**(1/3)
        print(f'{pi:.5f}')

else:

    for i in range(1, termos+8, 4):
        s += 1/(i)**3
        qtdTermos += 1

        if qtdTermos < termos:
            s -= 1/(i+2)**3
            qtdTermos += 1
        
    pi = (s*32)**(1/3)
    print(f'{pi:.5f}')