
altura = int(input().strip())

comprimento = int(input().strip())

largura = int(input().strip())

areaDoPiso = largura*comprimento

volumeDaSala = altura * comprimento * largura

alturaArea = 2 * altura * (largura +  comprimento)

print(f'{areaDoPiso}\n{volumeDaSala}\n{alturaArea}')

