def primo(n):
    if n <= 1:
        return False
    if n > 2 and n%2 == 0:
        return False
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True


numbers = [int(x) for x in input().split()]

produto = 1
count = 0
for i in range(4):
    if  primo(numbers[i]) is True:
        produto *= numbers[i]
        count += 1
    else:
        print('SEM PRODUTO')
        break

if count == 4:
    print(produto)