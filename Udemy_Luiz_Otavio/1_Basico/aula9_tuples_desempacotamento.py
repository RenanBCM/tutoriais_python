# -------->>>>>>>>>>> EXEMPLO 1 <<<<<<<<<<<<<<------------
# DESEMPACOTAMENTO
print('EXEMPLO 1 e 2 - DESEMPACOTAMENTO')

nomes = ['Renan', 'Jaqueline', 'Dagmar']

#Exemplo 1 Desempacotamento
nome1, nome2, nome3 = nomes

#Exemplo 2 Desempacotamento
nome4, nome5, nome6 = ['Bastos', 'Cunha', 'Menezes']

print('nome1: ', nome1, '- nome2: ', nome2, '- nome3: ', nome3, '- nome4: ', nome4, '- nome5: ', nome5, '- nome6: ', nome6)
print()

#Exemplo 3 Desempacotamento
print('EXEMPLO 3 - DESEMPACOTAMENTO COM RESTO')
nome7, *resto = ['Cristo', 'Jesus', 'Vive', 'Quem', 'Crer', 'Sera', 'Salvo']
print(nome7, resto)
print()

# -------->>>>>>>>>>> EXEMPLO 4 <<<<<<<<<<<<<<------------
# TUPLE
# UMA TUPLE É MUITO PARECIDA COM UMA LISTA
# EM UMA TUPLA NAO PRECISAMOS USAR COLCHETE COMO EM UMA LISTA.
# OS METODOS DE UMA LISTA FUNCIONAM EM UMA TUPLA

print('EXEMPLO 4 - TUPLE')

nomes_tupla = 'Renan', 'Jaqueline', 'Dagmar' # Uma tupla sem colchetes
sobrenomes_tupla = ('Bastos', 'Cunha', 'Menezes') # Uma tupla tbm pode ser criada com parenteses

print(nomes_tupla[0], sobrenomes_tupla[0], sobrenomes_tupla[1], sobrenomes_tupla[2])
print()

print('EXEMPLO 5 - CONVERTENDO UMA LISTA EM UMA TUPLE')

exemplo_lista = ['Renan', 'Jaqueline', 'Dagmar']
conversao_tuple = tuple(exemplo_lista)
print(type(exemplo_lista), type(conversao_tuple))

