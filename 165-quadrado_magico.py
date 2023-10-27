lines = int(input())

matrix = []
sum_matrix = set()

for i in range(lines):
    row = [int(x) for x in input().split()]

    sum_matrix.add(sum(row))

    matrix.append(row)

sum_diagonal1 = 0
sum_diagonal2 = 0
for i in range(lines):
    result = 0
    for elemento in matrix:
        result += elemento[i]

    sum_diagonal1 += matrix[i][i]
    sum_diagonal2 += matrix[i][(lines - 1) - i]

    sum_matrix.add(result)
    sum_matrix.add(sum(matrix[i]))


sum_matrix.add(sum_diagonal1)
sum_matrix.add(sum_diagonal2)

set_matrix = len(sum_matrix)

if set_matrix == 1:
    print(sum_diagonal1)
else:
    print('-1')
