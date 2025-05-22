# -------->>>>>>>>>>> EXEMPLO 1 <<<<<<<<<<<<<<------------

print('EXEMPLO 1 - FOR')

texto = 'Python'

for letra in texto:
    print(letra)

print('ACABOU EXEMPLO 1')
print()

# -------->>>>>>>>>>> EXEMPLO 2 - RANGE <<<<<<<<<<<<<<------------

print('EXEMPLO 2 - FOR COM RANGE')

range_1 = range(10)
range_2 = range(6, 10)
range_3 = range(6, 60, 6)


print('Imprimindo ',range_2)
for valor in range_2:
    print(valor)

print()

print('Imprimindo ',range_3)
for valor in range_3:
    print(valor)

print('ACABOU EXEMPLO 2')
print()

# -------->>>>>>>>>>> EXEMPLO 3 - BREAK, CONTINUE, ELSE <<<<<<<<<<<<<<------------

print('EXEMPLO 3 - BREAK, CONTINUE, ELSE')

for i in range(10):
    if i == 2:
       print('i é igual a 2, pulando...')
       continue

    if i == 8:
       print('i é igual a 8, else nao executara...')
       break

    for j in range(1, 3):
        print(i, j)
    
else:
    print('For completo com sucesso')