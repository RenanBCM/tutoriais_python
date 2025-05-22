# -------------- > DESEMPACOTAMENTO < -----------------

print('------------ > Desempacotando < ------------', '\n')

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}

# Desempacotamento das CHAVES
a, b = pessoa
print('Desempacotamento das CHAVES - ( a, b = pessoa )', '\n')
print(a, b, '\n')

# Desempacotamento das VALORES
a, b = pessoa.values()
print('Desempacotamento das VALORES - ( a, b = pessoa.values() )', '\n')
print(a, b, '\n')

# Desempacotamento dos ITENS
a, b = pessoa.items()
print('Desempacotamento das ITENS - ( a, b = pessoa.items() )', '\n')
print(a, b, '\n')

# -------------- > EMPACOTAMENTO < -----------------

print('------------ > Empacotando < ------------', '\n')

dados_pessoa = {
    'idade': 16,
    'altura':1.6,
}

# Empacotamento das CHAVES
empacotando_chaves = {*dados_pessoa}
print('Empacotamento das CHAVES - ( empacotando_chaves = {*dados_pessoa} )', '\n')
print(empacotando_chaves, '\n')

# Empacotamento das CHAVES e VALORES
empacotando_chaves_valores = {**dados_pessoa}
print('Empacotamento das CHAVES e VALORES - ( empacotando_chaves_valores = {**dados_pessoa} )', '\n')
print(empacotando_chaves_valores, '\n')





