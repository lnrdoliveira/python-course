"""
A calculator made with while
"""
while True:
    numero_1 = input('Digite o primeiro número: ')
    numero_2 = input('Digite o outro número: ')
    operador = input('Digite o operador (+-/*): ')
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Número(s) inválido(s).')
        continue

    operador_permitidos = ('+-/*')
    if operador not in operador_permitidos:
        print('Operador inválido.')
        continue
    if len(operador) > 1:
        print('Informe apenas um operador.')
        continue

    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = ', num_1_float + num_2_float)
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = ', num_1_float - num_2_float)
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = ', num_1_float / num_2_float)
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = ', num_1_float * num_2_float)
    else:
        print('Não deveria chegar aqui.')

    sair = input("Você quer [s]air?").lower().startswith('s')
    if sair is True:
        break