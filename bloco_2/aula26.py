"""
args - argumentos não nomeados
* - *args (empacotamento e desempacotamento) (convenção)
"""
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

def soma(*args): # (*args): Usado para passar uma quantidade ilimitada de argumentos não nomeados.
    total = 0 # Acumulador
    for numero in args:
        total += numero
    return total

soma(1, 2, 3, 4, 5, 6)
soma_1 = soma(4, 5, 6)
print(soma_1)