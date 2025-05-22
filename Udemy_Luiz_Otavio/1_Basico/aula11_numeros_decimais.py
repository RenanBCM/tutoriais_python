import decimal

# -------->>>>>>>>>>> EXEMPLO 1 <<<<<<<<<<<<<<------------

print('Exemplo 1 - ROUND')

numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2

print(numero_3)
print(round(numero_3))
print(round(numero_3,2), '\n')

# -------->>>>>>>>>>> EXEMPLO 2 <<<<<<<<<<<<<<------------
# utilizando a classe "decimal"

print('Exemplo 2 - Classe Decimal')

numero_4 = decimal.Decimal('0.1')
numero_5 = decimal.Decimal('0.7')
numero_6 = numero_4 + numero_5

print(numero_6)