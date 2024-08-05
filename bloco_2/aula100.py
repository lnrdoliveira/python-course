import copy
from dados import produtos

novos_produtos = [
    {**p, 'preco': round(p['preco'] * 1.1, 2)} 
    for p in copy.deepcopy(produtos)
    ]

print(*produtos, sep="\n")
print()
print(*novos_produtos, sep="\n")