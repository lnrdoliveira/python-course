# try, except, else e finally

#a = 18
#b = 0
#c = a / b

try:
    a = 18
    #b = 0
    print('linha 1')
    c = a / b
except ZeroDivisionError:
    print('sub by 0')
except NameError:
    print('nome errado')
    
print('continuar')