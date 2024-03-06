"""
CPF: 746.824.890-70

Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um doz valores por uma 
contagem regressiva começando de 10

Ex.: 746.824.890-70 (746824890)
    10  9   8   7   6   5   4   3  2    (Contagem regressiva)
*   7   4   6   8   2   4   8   9  0    (CPF)
______________________________________
    70  36  48  56  12  20  32  27 0    (Resultado)

Somar todos os resultados:
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9 (>9):
    Resultado é 0
contrário disso (<= 9):
    O resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
import re
import sys

# cpf_enviado_usuario = '746.824.890-70'\
#      .replace('.','')\
#      .replace(' ','')\
#      .replace('-','')
      #74682489070 - 746.824.890-70
entrada = input('cpf [746.824.890-70]: ')
cpf_enviado_usuario = re.sub(r'[^0-9]', '', entrada)

primeiro_char_input = entrada == entrada[0]*len(entrada)

if primeiro_char_input:
    print('Você enviou dados sequenciais')
    sys.exit()

print(entrada, primeiro_char_input)
nove_digitos = cpf_enviado_usuario[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
resultado_digito_2 = 0

# PRIMEIRO DÍGITO DO CPF
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0 

# SEGUNDO DÍGITO DO CPF
dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calc = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_usuario == cpf_gerado_pelo_calc:
    print('cpf valido')
else:
    print('invalido')