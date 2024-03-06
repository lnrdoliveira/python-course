"""
exercício
exiba os índices da lista
0 - maria
1 - helena
2 - luiz
"""

lista = ['maria', 'helena', 'luiz']
lista.append('leo')
#numero = 0
#for nome in lista:
#    print(f'{numero} - {nome}')
#    numero += 1

# ou
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))