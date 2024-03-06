"""
enumerate - enumera iteráveis  (ÍNDICES)
"""
lista = ['maria', 'helena', 'luiz']
lista.append('João')

lista_enum = enumerate(lista)

for item in lista_enum:
    print(item)