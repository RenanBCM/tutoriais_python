# Sets - Conjuntos em Python (Tipo Set)
# Conjuntos são ensinados na matematica
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutaveis, porem aceitam apenas tipos mutaveis como valor interno.

# Criando um set
# set(iteravel) ou {1, 2, 3}

set_vazio = set()
print(set_vazio, type(set_vazio), '\n')

# Perceba que SET's não garantem ordem.
set_nome = set('Jesus')
print(set_nome,  ' - Tipo Set() não tem ordem - ', type(set_nome), '\n')

# Perceba que SET's não garantem ordem.
set_salvador = {'Senhor e Salvador', 777, 33}
print(set_salvador, ' - Tipo Set() não tem ordem - ', type(set_salvador), '\n')

# Sets são eficientes para remover valores duplicados de iteraveis.
set_duplicado = {1, 2, 3, 3, 3, 3, 3, 4, 5, 5, 5, 6, 7, 7}
print(set_duplicado, ' - Tipo Set() não DUPLICA - ', type(set_duplicado), '\n')

# Convertendo Lista em Set()
lista1 = [1, 2, 3]
print(lista1, type(lista1), '\n')

lista1_set = set(lista1)
print(lista1_set, type(lista1_set), '\n')

# Sets são iteraveis (for, in, not in)
for numero in lista1_set:
    print(numero)

# Metodos uteis:
# add, update, clear, discard

lista1_set.add('Jesus')
lista1_set.update('Salvador')
print('Metodos add() e update() executados no Set()')
print(lista1_set, type(lista1_set), '\n')

lista1_set.discard('S')
lista1_set.discard('a')
lista1_set.discard('l')
lista1_set.discard('v')
lista1_set.discard('d')
lista1_set.discard('o')
lista1_set.discard('r')
print('Metodos discard() executado no Set()')
print(lista1_set, type(lista1_set), '\n')

# Operadores Uteis

s_OP_1 = {1, 2, 3}
s_OP_2 = {2, 3, 4}
s_OP_3 = s_OP_1 | s_OP_2
s_OP_4 = s_OP_1 & s_OP_2

print('Operador " | " executa um UNION - s_OP_3 = s_OP_1 | s_OP_2 - ', s_OP_3, '\n')
print('Operador " & " Retorna os itens presentes em ambos os sets - s_OP_4 = s_OP_1 & s_OP_2 - ', s_OP_4, '\n')