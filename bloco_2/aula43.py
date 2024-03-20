# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

lista = []
for numero in range(10):
    lista.append(numero)

lista = [
    numero * 2
    for numero  in range(10)
]
print(list(range(10)))
print(lista)

# Mapeamento de dados em list comprehension
produtos = [
    {'nome': 'p1', 'preco': 10, },
    {'nome': 'p2', 'preco': 20, },
    {'nome': 'p3', 'preco': 30, },
]
novos_produtos = [
    {**produto, 'preco': produto['preco']*1.05} #alterando a chave preco, aumento de 5% em cada produto
    if produto['preco'] > 20 else {**produto} # if ternario para aumentar o preco somente em precos maiores que 20
    for produto in produtos
]
print(novos_produtos)
print(*novos_produtos, sep='\n')