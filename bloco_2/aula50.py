"""
Introdução à generator functions em python
generator = (n for n in range(1000000))
"""

def generator(n=0):
    yield 1 # pausa a function aqui
    print('continuando...')
    yield 2 # pausa
    print('mais uma...')
    yield 3
    print('terminando')
    return 'acabou'

gen = generator(n=0)
for n in gen:
    print(n)