"""
Exercício com funções

1) Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável

2) Crie uma função que fale se o número é par ou ímpar.
Retorne se o número é par ou ímpar
"""

# 2:
def odd_even(x):
    oddevencheck = x % 2 == 0
    if oddevencheck: # bool check
        return f'{x} é par'
    return f'{x} é ímpar'

user_input = int(input("Qual número você quer testar? "))
func_output = odd_even(user_input)
print(func_output)

# 1:
def multiply(*args):
    total = 1
    for nums in args:
        total *= nums

    return total

re_multiply = multiply(1, 2, 3, 4, 5)
print(re_multiply)