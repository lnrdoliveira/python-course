import random
import string

def generate_secure_password(length=12, include_uppercase=True, include_numbers=True, include_symbols=True):
    characters = string.ascii_lowercase
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    
    secure_password = ''.join(random.choice(characters) for _ in range(length))
    return secure_password

if __name__ == "__main__":
    password_length = int(input("Digite o comprimento da senha desejada: "))
    uppercase_option = input("Incluir letras maiúsculas? (s/n): ").lower() == 's'
    numbers_option = input("Incluir números? (s/n): ").lower() == 's'
    symbols_option = input("Incluir símbolos? (s/n): ").lower() == 's'

    secure_password = generate_secure_password(password_length, uppercase_option, numbers_option, symbols_option)
    print("Senha gerada:", secure_password)
