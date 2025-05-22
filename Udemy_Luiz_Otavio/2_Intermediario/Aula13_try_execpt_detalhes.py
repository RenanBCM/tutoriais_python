
print('---------- Exemplo 3 Try Except - 2 CLASSES ou MAIS ---------- ','\n')

a = 10
b = 0
c = 20

# Erro Divisão por ZERO
try:
    # Erro Index
    print('Linha 1'[1000])

# Com o "as error" no final posso saber qual erro ocorreu.
except (IndexError) as error:
    print('MSG:         ', error)
    print('Nome Classe: ', error.__class__.__name__, '\n')


