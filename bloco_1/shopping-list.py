"""
Faça uma lista de compra com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores de sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista
"""
import os 

lista = []

while True:
    option = input("Selecione uma opção \n [I]nserir - [A]pagar - [L]istar: ").lower()
    allowed_options = ('ial')
    inp = ''
    if option not in allowed_options:
        print('Opção inválida.')
        continue
    if option == 'i':
        os.system('cls')
        inp = input("O que você deseja inserir na lista?")
        lista.append(inp)
    elif option == 'a':
        os.system('cls')
        inp = input("Qual índice do que você quer apagar?")
        try:
            inp_a = int(inp)
            del lista[inp_a]
        except ValueError:
            print("Não foi possível apagar esse índice.")
        except IndexError:
            print("Esse índice não existe.")
        except Exception:
            print("Erro desconhecido.")

    elif option == 'l':
        os.system('cls')
        if len(lista) == 0:
            print('Não há nada em sua lista.')
        for i, valor in enumerate(lista):    
            print(i, valor)