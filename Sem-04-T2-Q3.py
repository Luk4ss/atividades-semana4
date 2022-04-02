
def porcentagem(valor, percentual):
    return valor* (percentual/100)


valor = float(input().strip())

percentual = porcentagem(valor, float(input().strip()))

valorComAumento = valor + percentual

valorComDesconto = valor - percentual

print(f'{valorComAumento:.2f}\n{valorComDesconto:.2f}')