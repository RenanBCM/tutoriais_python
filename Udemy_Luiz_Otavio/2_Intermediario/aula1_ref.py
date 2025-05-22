# -------->>>>>>>>>>> FUNCOES <<<<<<<<<<<<<<------------

# -------->>>>>>>>>>> EXEMPLO 1 - Com Argumento Nomeado e Não Nomeado <<<<<<<<<<<<<<------------

# Uma FUNCAO por padrão retorna NONE (Nada)
# Para definir uma funcao no python utilizamos a palavra "def"
# Exemplo Argumento Nomeado " def( c='O Pão Da Vida' ) "
# Exemplo Argumento Não Nomeado " def( c ) "

print('Exemplo 1 - Funções Com Argumento Nomeado e Não Nomeado', '\n')

def cristo(a, b, c='O Pão Da Vida'):
    print('Jesus ', a, b, c)

cristo('Meu Senhor,', 'Meu Resgate,', 'Meu Salvador')
cristo('Meu Senhor,', 'Meu Resgate,')
print()

# -------->>>>>>>>>>> EXEMPLO 2 <<<<<<<<<<<<<<------------

# Utilizando None Como Argumento Nomeado

print('Exemplo 2 - NoneType e None', '\n')

def cristo_senhor(aa, bb, cc=None):
    if cc is not None:
        print(f'{aa=} {bb=} {cc=}', ' - ' , aa + bb + cc)
    else:
        print(f'{aa=} {bb=}', ' - ' , aa + bb )

cristo_senhor('Meu Senhor,', 'Meu Resgate,', 'Meu Salvador')
cristo_senhor('Meu Senhor,', 'Meu Resgate,')
print()

