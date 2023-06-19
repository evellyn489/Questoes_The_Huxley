ph = int(input('Digite o pH da solucao:\n'))

if 0<=ph<=14:
    if ph < 7:
        print('Essa solucao e acida.')
    elif ph > 7:
        print('Essa solucao e basica.')
    else:
        print('Essa solucao e neutra.')
else:
    print('Valor deve estar entre 0 e 14.')