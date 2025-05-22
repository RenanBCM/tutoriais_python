# -------->>>>>>>>>>> EXEMPLO 1 <<<<<<<<<<<<<<------------
# O LIST é como se fosse um array, uma matriz.
print('EXEMPLO 1 - LISTA')

texto = 'ABCDE'

# podemos criar uma lista de dois jeitos
# 1- utilizando a função list()
# 2 - E utilizando colchetes.

lista_1 = list()
print(lista_1, ' - lista vazia, portanto lista tipo ',type(lista_1))
print()

# -------->>>>>>>>>>> EXEMPLO 2 <<<<<<<<<<<<<<------------

print('EXEMPLO 2 - VALORES E TIPOS DENTRO DE UMA LISTA')

lista_2 = [123, True, 'Renan', 1.2, []]
print(lista_2)
print()

for item_lista in lista_2:
    print(item_lista, ' - ', type(item_lista))
print()
# -------->>>>>>>>>>> EXEMPLO 3 <<<<<<<<<<<<<<------------

# Um CRUD seria ( CREATE, READ, UPDATE, DELETE ) - ( CRIAR, LER, ALTERAR, APAGAR)
print('EXEMPLO 3 - CRUD')

lista_3 = [10, 20, 30, 40]
print('imprimindo lista inteira: ', lista_3)

numero = lista_3[2]
print('Acessando uma posisão da matriz atraves do indice: ', numero)
print()

# -- UPDATE --
print('UPDATE - CRUD')
lista_3[2] = 777
print(lista_3)
print()

# -- DELETE --
print('DELETE - CRUD')

# O Metodo del() remove o elemento por indicie da lista
del lista_3[2]

# O Metodo pop() remove o ultimo elemento da minha lista
lista_3.pop()

print(lista_3)
print()

# -- INSERT --
print('INSERT - CRUD')

# O Metodo append() adicioona um elemento no final da minha lista.
lista_3.append(50)
print(lista_3)

# O Metodo insert() adicioona um elemento na lista.
# Ele recebe dois argumentos
# Argumento 1 - Temos que passar o indice do valor inserido.
# Argumento 2 - O valor inserido na lista.
lista_3.insert(0, 777)
print(lista_3)
print()

# -------->>>>>>>>>>> EXEMPLO 4 <<<<<<<<<<<<<<------------

# CONCATENANDO LISTAS
print('EXEMPLO 4 - CONCATENANDO E ESTENDENDO LISTA')

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

# primeira forma de concatenar listas
# utilizando o +
lista_c = lista_a + lista_b
print('Primeira forma de de concatenar listas com "+": ')
print(lista_c)
print()

# Segunda forma de concatenar listas
# Utilizando a funcao extend()
# A funcao extend() estende a lista_b na lista_a.
# Ou seja ela alrtera diretamente a lista_a
lista_d = lista_a.extend(lista_b)
print('Não podemos concatenar listas na forma abaixo: ')
print('lista_d = lista_a.extend(lista_b)')
print('Pois o resultado sera "None"')
print(lista_d)
print()

print('A forma correta seria: ')
print('lista_a.extend(lista_b)')
print(lista_a)
print()

# -------->>>>>>>>>>> EXEMPLO 5 <<<<<<<<<<<<<<------------

# CONCATENANDO LISTAS
print('EXEMPLO 5 - COPIANDO LISTAS')

lista_original = [1, 2, 3]
print('lista_original ANTES da alteração: ', lista_original)


lista_copia = lista_original.copy()
lista_original[0] = 777

print('Mesmo alterando lista original a lista_copia não alterou: ', lista_copia)
print('lista_original DEPOIS da alteração: ', lista_original)
print()

# -------->>>>>>>>>>> EXEMPLO 6 <<<<<<<<<<<<<<------------

print('EXEMPLO 6 - FOR COM LISTAS')

lista_for = ['Renan', 'Jaqueline', 'Dagmar']

for nome in lista_for:
    print(nome)


