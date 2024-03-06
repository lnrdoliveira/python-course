"""
Introdução ao desempacotamento + tuples (tuplas)
_ é uma convenção que os desenvolvedores usam para sinalizar que aquela variável 
não vai ser utilizada
"""
_, nome1, *_ = ['maria', 'helena', 'luiz'] #aqui está pegando o segundo lugar da lista (helena)
print(nome1)
