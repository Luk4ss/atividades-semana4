
def inverter(n):
    u = n % 10

    n = n // 10

    d = n % 10

    n = n // 10

    c = n % 10

    n = n //10

    m = n % 10

    return (u * 1000) + (d * 100) + (c *10) + m



numero = int(input().strip())


print(f'{inverter(numero)}')

