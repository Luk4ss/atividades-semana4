horas = int(input().strip())
minutos = int(input().strip())
segundos = int(input().strip())

horasEmsegundos = horas*3600

minutosEmsegundos = minutos*60

totalDeSegundos = horasEmsegundos + minutosEmsegundos + segundos

print(f'{totalDeSegundos}')