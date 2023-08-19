while True:
    num1 = int(input())

    if not(1<=num1<=9):
        print('Insira um número inicial entre 1 e 9')
    else:
        break
    
while True:
    num2 = int(input())

    if not(1<=num2<=9):
        print('Insira um número final entre 1 e 9')
    else:
        break

if num1 > num2:
    print('Nenhuma tabuada nesse intervalo')

else:
    for i in range(num1, num2+1):
        for j in range(1, 10):
            resultado = j * i
            
            print(f'{i} x {j} = {resultado}')
        print()