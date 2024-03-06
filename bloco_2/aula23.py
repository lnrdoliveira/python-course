"""
Valores padrão por parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
"""

# O Z pode ser definido como 0, no entanto, se o usuário der input em um Z na variável Z
# Ele vai reconher o 0 como não valor (Igual ao None).
# Por isso usar o None e checar ele em um if com 'is not None'

def soma(x, y, z = None):
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z)
    else:
        print(f'{x= } {y=}', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(100, 200, 0)