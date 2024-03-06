entrada = input('Digite a hora em números inteiros: ')
'''
0-11 = Bom dia
12-17 = Boa tarde
18-23 = Boa noite
'''

try:
    hora = int(entrada)
    if hora >= 0 and hora <= 11:
        print('bom dia')
    elif hora <= 17:
        print('boa tarde')
    elif hora <= 23:
        print('boa noite')
    else:
        print('não conheco essa hora')
except:
    print('Você não informou um input correto')