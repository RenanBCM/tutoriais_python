# -------->>>>>>>>>>> EXEMPLO 1 <<<<<<<<<<<<<<------------
# ENUMERATE
# TEM A FUNCAO DE ENUMERAR A MINHA LISTA, COLOCANDO INDICES ANTES DOS VALORES, PRATICAMENTE TRANSFORMANDO A LISTA EM UMA TUPLA
# ENUMERATE ENUMERA ITERAVEIS

print('EXEMPLO 1 - ENUMERATE')

lista = ['Cristo', 'Jesus', 'Vive', 'Quem', 'Crer', 'Sera', 'Salvo']
lista_enumerada = enumerate(lista)


print('Primeiro valor ENUMERATE: ', next(lista_enumerada)) # Primeiro valor imprimido virou uma tupla
print('Imprimindo um ENUMERATE: ', lista_enumerada)
print()

print('Podemos utilizar o for no inumerate:')
for item in lista_enumerada:
    print(item)
print()

# -------->>>>>>>>>>> EXEMPLO 2 <<<<<<<<<<<<<<------------

print('EXEMPLO 2 - ENUMERATE DIRETO NO FOR')

lista_2 = ['Cristo', 'Jesus', 'Vive', 'Quem', 'Crer', 'Sera', 'Salvo']

print('Inumerate direto no for: ')
for item_enu in enumerate(lista_2):
    print(item_enu)

print('Imprimindo um ENUMERATE Convertido em Tupla: ', tuple(lista_2), '\n')

# -------->>>>>>>>>>> EXEMPLO 3 <<<<<<<<<<<<<<------------

print('EXEMPLO 3 - Enumerate com Start')
lista_3 = ['Cristo', 'Jesus', 'Vive', 'Quem', 'Crer', 'Sera', 'Salvo']

lista_enumerate = list(enumerate(lista_3, start=19))

print('Inumerate com Start: ')
for item_enu in enumerate(lista_enumerate):
    indice, valor = item_enu
    print(indice, valor)
