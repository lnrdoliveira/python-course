"""
Introdução às funções (def) em python
Funções são trechos de códigos usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções python retornam None (nada).=
"""

# def Print(a, b, c):
#     print('veio da function')

# def imprimir(a, b, c):
#     print(a+b+c)

# imprimir(2, 3, 4)

def saudacao(nome = 'sem nome'):
    print(f'Olá, {nome}!')

saudacao('Leo')
saudacao('Rafa')
saudacao('Ju')
saudacao()