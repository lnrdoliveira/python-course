# isinstance - para saber se o objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2), {0, 1}, {'nome': 'luiz'},
]

for item in lista:
    if isinstance(item, set):
        print('set')
        item.add(5)
        print(item, isinstance(item, set))

    if isinstance(item, str):
        print('str')
        print(item.upper(), isinstance(item, set))

    if isinstance(item, (int, float)): #int ou float
        print('num')
        print(item, item * 2)
    else:
        print('outro')
        print(item)
