# -------->>>>>>>>>>> EXEMPLO 1 <<<<<<<<<<<<<<------------

print('-------->>>>>>>>>>> Exemplo 1 - Dicionarios <<<<<<<<<<<<<<------------', '\n')

# Dicionarios em Python (tipo dict)
# Dicionarios sao estruturas de dados do tipo:
#       pra de "CHAVES" e "VALOR"
# Usamos as chaves { } ou a Classe dict para criar DICIONARIOS
# Imutaveis: str, int, float, bool, tuple.
# Mutavel: dict, list

pessoa = {
    'nome': 'Jesus Cristo',
    'sobrenome': 'Nazareno Filho do Deus Vivo',
    'idade': 33,
    'altura': 1.8,
    'endereços': [
        {'rua':'Jerusalem', 'numero': 123},
        {'rua':'Cafarnaum', 'numero': 345}
    ]
}

print(pessoa,'\n')

#Accesando Dicionario.

print(pessoa['nome'],'\n')

#Acessando Iterando o Dicionario

for chave in pessoa:
    print(chave,': ',pessoa[chave])
print()

# -------->>>>>>>>>>> EXEMPLO 2 <<<<<<<<<<<<<<------------

print('-------->>>>>>>>>>> Exemplo 2 - Incluindo Chaves <<<<<<<<<<<<<<------------', '\n')

# Dicionario Vazio.
salvador = {}

# Adicionando uma chave.
salvador['nome'] = 'Jesus de Nazare'

# Adicionando uma chave com VARAIVEL
chave_2 = ' O Pão Da Vida'
salvador[chave_2] = ' aquele que vem a mim não terá fome. - João 6:35'

# Deletando uma chave.
salvador['CHAVE_DELETAR'] = 'CHAVE_DELETAR'
print(salvador['CHAVE_DELETAR'], " - del salvador['CHAVE_DELETAR'] ",'\n')

del salvador['CHAVE_DELETAR']

print(salvador, '\n')

# -------->>>>>>>>>>> EXEMPLO 3 <<<<<<<<<<<<<<------------

print('-------->>>>>>>>>>> Exemplo 3 - Metodo GET() <<<<<<<<<<<<<<------------', '\n')

print(salvador.get('nome'))
print(salvador.get(' O Pão Da Vida'))
print(salvador.get('x'))
print(salvador.get('x', 'Nao foi encontrado essa chave'))  