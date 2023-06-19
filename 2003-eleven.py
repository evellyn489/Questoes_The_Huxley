numero = int(input())


fibonacci = []

for i in range(numero):
    if i >= 2:
        sequencia = fibonacci[i-1] + fibonacci[i-2]
        fibonacci.append(sequencia)
    else:
        fibonacci.append(1)

string = ''
for elemento in range(numero):
    if elemento+1 in fibonacci:
        string += 'O'
    else:
        string += 'o'
print(string)