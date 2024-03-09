"""
Exercício visto em um vídeo no canal do Augusto Galego com participação Leonardo Menezes
Imprimir os n primeiros números da sequência fibonacci.
A quantidade deve vir de um input do usuário
"""

# 1 1 2 3 5 8 13 21
def fibonacci(num):
    if num >= 1:
        res = [1]
        prev, curr = 1, 1
        for i in range(num):
            res.append(curr)
            curr, prev = curr + prev, curr
        print(res)
        return res
    elif num < 0:
        raise Exception('Número precisa ser positivo')


n = int(input('Quantos números você quer mostrar? '))
fibonacci(n)
