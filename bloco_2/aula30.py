"""
criar uma função que multiplique um número por 2, 3 e 4
"""

def create_multiplier(mult):
    def multiplier(num):
        return num * mult
    return multiplier


double = create_multiplier(2)
triple = create_multiplier(3)
quadruple = create_multiplier(4)

print(double(2))
print(triple(2))
print(quadruple(2))