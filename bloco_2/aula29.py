"""
closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao, nome):
    def saudar():
        return f'{saudacao}, {nome}!'
    return saudar

s1 = criar_saudacao('bom dia', 'luiz')
s2 = criar_saudacao('boa noite', 'leo')
print(s1)
print(s2)