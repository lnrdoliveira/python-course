def verifica_palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]

entrada = input("Digite uma palavra para verificar se é um palíndromo: ")
if verifica_palindromo(entrada):
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")