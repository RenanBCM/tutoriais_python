# >>>>>>>>>>>>>>>> Generator expression, Iterables e Iterators <<<<<<<<<<<<<<<<<<<

# Iterável = O Iterável tem responsabilidade de deter os valores sequêncialmente.

# Iterator = Somente te entregar um valor por vez.
#            Ele vai te entregar o proximo valor sem saber o valor anterior ou o proximo.

# Generator = São funções que sabem pausar em determinadas ocasiões
#             Todo Generator é um Iterator tbm

import sys

iterable = ['Jesus','Cristo','Salvador']
iterator_1 = iterable.__iter__()
iterator_2 = iter(iterable)

print(next(iterator_1))
print(next(iterator_1))
print(next(iterator_1), '\n')

generator_1 = [n for n in range(10)]
print(generator_1, '\n')

generator_2 = (n for n in range(10))
print(generator_2, '\n')

# Tamanho em Bytes Generator
print(sys.getsizeof(generator_1), '\n')

for n in generator_1:
    print(n)