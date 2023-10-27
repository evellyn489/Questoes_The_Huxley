while True:
    pessoas_sequencias = {}

    pessoas, sequencias_dna = [int(x) for x in input().split()]

    if pessoas==sequencias_dna==0:
        break
    
    for i in range(pessoas):
        sequencia = str(input())

        if sequencia in pessoas_sequencias:
            pessoas_sequencias[sequencia] += 1
        else:
            pessoas_sequencias[sequencia] = 0

    for p in range(pessoas):
        c = 0
        for v in pessoas_sequencias.values():
            if v == p:
                c += 1
        print(c)