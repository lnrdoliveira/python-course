"""
Manipulando chaves e valores em dicionários (dict)
"""
pessoa = {
}

chave = 'nome'
pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'


print(pessoa)
print(pessoa[chave])
pessoa[chave] = 'maria'
del pessoa['sobrenome']
print(pessoa)