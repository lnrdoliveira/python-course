"""
Generator expression, iterables e iterators em python
"""
import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__
lista = [n for n in range(10)]
generator = (n for n in range(10))
print(lista)
print(generator)
print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

for n in generator:
    print(n)