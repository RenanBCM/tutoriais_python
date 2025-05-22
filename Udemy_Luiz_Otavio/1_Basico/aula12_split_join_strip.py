# -------->>>>>>>>>>> EXEMPLO 1 - SPLIT <<<<<<<<<<<<<<------------

# SPLIT - Divide uma String
# JOIN - Une uma string

frase = 'Porque a palavra da cruz é loucura para os que perecem.'

lista_palavras = frase.split(' ')

print('----- EXEMPLO 1 - SPLIT ----- ')
print(frase, '\n')
print('Lista com a frase abaixo: ')
print(lista_palavras, '\n')

# -------->>>>>>>>>>> EXEMPLO 2 <<<<<<<<<<<<<<------------

# STRIP deleta os espaços no começo e no fim.
# RSTRIP deleta os espaços da direits.
# LSTRIP deleta os espaços da esquerda.

print('----- EXEMPLO 2 - STRIP COM FOR ----- ')

frase_2 = 'O justo vivera pela fé'

lista_frase_2 = frase_2.split(' ')

for i, frase_2 in enumerate(lista_frase_2):
    print(lista_frase_2[i].strip())

print('Lista com a frase abaixo: ')
print(lista_frase_2, '\n')

# -------->>>>>>>>>>> EXEMPLO 3 <<<<<<<<<<<<<<------------
# JOIN - Une uma string

print('----- EXEMPLO 3 - JOIN ----- ')

frase_unidas = ''.join('abc')
frase_unidas_2 = '-'.join('abc')
frase_unidas_3 = '='.join('abc')

print(frase_unidas)
print(frase_unidas_2)
print(frase_unidas_3)

frase_join = '-'.join(lista_palavras)
print(frase_join)

