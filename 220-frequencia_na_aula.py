estudantes = int(input())

presentes = set()
for i in range(estudantes):
    frequencia = int(input())
    presentes.add(frequencia)

qtd_presentes = len(presentes)
print(qtd_presentes)