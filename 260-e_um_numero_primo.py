def primo(n):
    if n <= 1:
        return False
    if n > 2 and n % 2 == 0:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

while True:
    numero = int(input())
    if numero == -1:
        break
    if primo(numero) is False:
        print(0)
    else:
        print(1)