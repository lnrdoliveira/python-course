"""
Retorno de valores das funções (return)
Alimenta a variável onde a função foi chamada 
com o resultado da operação de dentro da função
"""

def soma(x, y):
    bagulho = x + y
    return bagulho

soma1 = soma(2, 2)
soma2 = soma(3, 3) 
print(soma1, soma2)