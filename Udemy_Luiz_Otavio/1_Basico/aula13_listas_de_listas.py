# -------->>>>>>>>>>> EXEMPLO 1 - SPLIT <<<<<<<<<<<<<<------------

print('EXEMPLO 1 - IMPRIMINDO LISTAS')

salas = [
# Indices -      0        1
             ['Maria', 'Helena',],                              # 0
# Indices -      0        1
             ['Elaine',],                                       # 1
# Indices -      0        1         2             3
             ['Luiz', 'Roberto', 'Garro', (0, 10, 20, 30, 40)], # 2
]

print(salas[1][0])
print(salas[2][3][3], '\n')

print('EXEMPLO 2 - ITERANDO LISTAS DENTRO DE LISTAS')

for sala in salas:
    print(f'A sala é: {sala}')
    for item in sala:
        print(f'Aluno: {item}')