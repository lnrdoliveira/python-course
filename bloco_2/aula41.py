# Empacotamento e desempacotamento de dicionários (dict)

a, b = 1, 2 #Desempacotando
a, b = b, a

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}
dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}
# (a1, a2), (b1, b2) = pessoa.items()
# print(a1, a2)
# print(b1, b2)
# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa_completa = {**pessoa, **dados_pessoa}
# print(pessoa_completa)
def mostra_argumentos(*args, **kwargs):
    print('NÃO NOMEADOS: ', args) #Exibe os argumentos não nomeados
    for chave, valor in kwargs.items():
        print(chave, valor)

#mostra_argumentos(1, 2, nome='Joana', qlq=123)
mostra_argumentos(**pessoa_completa)