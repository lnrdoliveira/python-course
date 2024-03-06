"""
métodos de string
split e join com list e str
split - divide uma string
join - une uma string
strip - corta dos dois lados
rstrip - corta espaço da direta (right)
lstrip - corta espaço da esquerda (left)
"""
frase = "Olha só que      , coisa interessante.      "
lista_frases = frase.split(',')

for i, frase in enumerate(lista_frases):
    lista_frases[i] = lista_frases[i].strip()

print(lista_frases)