"""
Lista comprehension em Python
Lista comprehension é uma forma rápida para criar listar
a partir de iteráveis
"""

#print(list(range(10)))

lista = []

for numero in range(10):
    lista.append(numero)

#print(lista)


lista = [
    #Dentro deste for está, ele está fazendo a lógica da linha abaixo
    numero * 10
    for numero in range(10)
] # Sempre a esquerda
print(lista)