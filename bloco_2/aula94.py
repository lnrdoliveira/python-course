# try, except, else e finally

try:
    print('Abrir arquivo')
    9/0
except ZeroDivisionError:
   print('bad code')
else:
    print('nao deu erro')
finally:
    print('Fechar arquivo')