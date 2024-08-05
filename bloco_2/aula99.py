import sys

import aula99_package.modulo
from aula99_package import modulo
from aula99_package.modulo import soma_do_modulo

print(soma_do_modulo(1,2))
print(aula99_package.modulo.soma_do_modulo(2,3))
print(modulo.soma_do_modulo(5,4))
print(soma_do_modulo(8,1))