
minutos = int(input().strip())

horas = minutos // 60

minutos = minutos % 60

print(f'{horas}:{minutos}')