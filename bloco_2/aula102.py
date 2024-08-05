# Funções decoradoras e decoradores
# Decorar = adicionar / remover / restringir / alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usdos para fazer o Python
# usar as funções decoradas em outras funções
# Decoradores são "syntax sugar"  (açúcar sintático)

def criar_funcao(func):
    def interna(*args, **kwargs):
        print("Vou te decorar")
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada.')
        return resultado
    return interna

#@criar_funcao
def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isistance(param, str):
        raise TyperError('param deve ser uma string')



invertida = inverte_string('123')
print(invertida)