segundos = int(input())

horas = segundos/3600
resto = float(segundos%3600)

minutos = int(resto/60)

segundos = int(resto%60)

print('%d h %d m %d s' %(horas, minutos, segundos))
