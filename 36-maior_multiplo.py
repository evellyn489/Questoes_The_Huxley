n1 = int(input())
n2 = int(input())

multiplo = 0
for i in range(n1+1, n2+1):
    if i % n1 == 0:
        multiplo = i

if multiplo == 0:
    print(f'sem multiplos menores que {n2}')
else:
    print(multiplo)