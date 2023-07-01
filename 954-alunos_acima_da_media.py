n = int(input())

todos_alunos = []

pontuacao = 0

for i in range(n):
    matricula = int(input())
    nome = input()
    nota = float(input())

    aluno = {"matrícula": matricula, "nome": nome, "nota": nota}
    pontuacao += nota

    todos_alunos.append(aluno)

media = pontuacao/n

ordenacao = sorted(todos_alunos, key=lambda x:(x["nota"], x["matrícula"]))

for individuo in ordenacao:
    if individuo["nota"] > media:
        print('Matricula: %.i Nome: %s Nota: %.1f' % (individuo["matrícula"], individuo["nome"], individuo["nota"]))

print('Media = %.2f' %media)

