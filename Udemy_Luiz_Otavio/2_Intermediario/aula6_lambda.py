# Função Lambda.
# São funções anonimas que contem apenas uma linha.
# Tudo deve ser contido dentro de uma unica expressão.

lista = [
    {'nome': 'Jesus', 'sobrenome': 'Cristo'},
    {'nome': 'Messias', 'sobrenome': 'Prometido'},
    {'nome': 'Resgate', 'sobrenome': 'Misericordioso'}
]

# -------->>>>>>>>>>> EXEMPLO 1 - lambda <<<<<<<<<<<<<<------------

print('Exemplo 1 lambda','\n')

lista.sort(key=lambda item:['nome'])

for item in lista:
    print(item)

print(lista,'\n')

# -------->>>>>>>>>>> EXEMPLO 2 - lambda <<<<<<<<<<<<<<------------

print('Exemplo 2 lambda','\n')

l_nome = sorted(lista, key=lambda item: item['nome'])
l_sobrenome = sorted(lista, key=lambda item: item['sobrenome'])

def exibir(lista):
    for item in lista:
        print(item)

print(exibir(l_nome))


