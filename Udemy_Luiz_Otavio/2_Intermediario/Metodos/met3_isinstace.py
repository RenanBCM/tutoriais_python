# -------->>>>>>>>>>> isinstace() <<<<<<<<<<<<<<------------

# isinstace() - Uma FUNCAO usada para saber se o objeto é de determinado tipo.

# SINTAXE
# isinstace(ITEM ITERAVEL, TIPO DE OBEJTO)

lista = ['Jesus',1, 1.1, 33, True, [0, 1, 2], (1, 2), {0,1}, {'nome':'Luiz'},'Cristo']

# -------->>>>>>>>>>> EXEMPLO 1 - isinstace() FLOAT <<<<<<<<<<<<<<------------

print('Exemplo 1 - isinstace() FLOAT', '\n')

for item in lista:
    # isinstace(ITEM ITERAVEL, TIPO DE OBEJTO)
    if isinstance(item, float):
        print(item, ' - ', isinstance(item, float), '\n')

# -------->>>>>>>>>>> EXEMPLO 2 - isinstace() String <<<<<<<<<<<<<<------------

print('Exemplo 2 - isinstace() STRING', '\n')

for item in lista:
    # isinstace(ITEM ITERAVEL, TIPO DE OBEJTO)
    if isinstance(item, str):
        print(item, ' - ', isinstance(item, str), '\n')

# -------->>>>>>>>>>> EXEMPLO 3 - isinstace() NUMBER e FLOAT <<<<<<<<<<<<<<------------

print('Exemplo 3 - isinstace() INT e FLOAT', '\n')

for item in lista:
    # isinstace(ITEM ITERAVEL, TIPO DE OBEJTO)
    if isinstance(item, (int, float)):
        print(item, ' - ', isinstance(item, (int, float)), '\n')