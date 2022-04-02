
def areaQuadrado(lado):
    return lado*lado

def perimetroQuadrado(lado):
    return lado * 4

lado = float(input().strip())

print(f'{areaQuadrado(lado):10.4f}\n{perimetroQuadrado(lado):10.4f}')