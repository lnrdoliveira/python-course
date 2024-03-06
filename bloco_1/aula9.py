entrada = input('Digite seu nome: ')

entrada_len = len(entrada)
print(f'O nome {entrada} tem {entrada_len} digitos.')

if entrada_len <= 4:
    print('short name')
elif entrada_len <= 6:
    print('normal name')
else:
    print('longest name')
