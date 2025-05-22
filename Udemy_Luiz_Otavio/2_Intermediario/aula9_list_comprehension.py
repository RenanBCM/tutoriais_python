# -------------- > List Comprehension < -----------------

# Lista Comprehension é uma forma rapida para criar listas

print('------------ > List Comprehension < ------------', '\n')

# -------->>>>>> EXEMPLO 1 - Populando Padrão <<<<<<<<<<<<<<------------

print('Exemplo 1 - Padrão Mais Usado de Popular Lista ')
print('populando lista vazia com .append() no for ', '\n')

lista_padrao = []
for numero in range(10):
    lista_padrao.append(numero)

print('Print da lista padrão: ', lista_padrao,  '\n')

# -------->>>>>> EXEMPLO 2 - RANGE <<<<<<<<<<<<<<------------

print('Exemplo 2 - RANGE ')
print('populando lista por range - "list(range(10))" ', '\n')
print(list(range(10)),  '\n')

# -------->>>>>> EXEMPLO 3 - Lista Comprehension INCOMPLETA <<<<------------

print('Exemplo 3 - Lista Comprehension INCOMPLETA ')
print('populando lista - "lista = [1 for numero in range(10)]" ', '\n')

lista_incompleta = [1 for numero in range(10)]
print(lista_incompleta, '\n')

# -------->>>>>> EXEMPLO 4 - Lista Comprehension COMPLETA <<<<------------

print('Exemplo 4 - Lista Comprehension COMPLETA ')
print('populando lista - "lista = [numero for numero in range(10)]" ', '\n')

lista_completa = [numero for numero in range(10)]
print(lista_completa)







