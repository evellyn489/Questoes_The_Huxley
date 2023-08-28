todos_livros = []

n = int(input())

for i in range(n):
    livro = input()
    todos_livros.append(livro)

ultimo_livro = input()

if ultimo_livro in todos_livros:
    print('Sim')
else:
    print('Não')