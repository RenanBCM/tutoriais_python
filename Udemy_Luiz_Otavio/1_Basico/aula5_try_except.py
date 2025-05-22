# -------->>>>>>>>>>> EXEMPLO 1 <<<<<<<<<<<<<<------------

print('EXEMPLO 1 - TRY EXCEPT')
numero_string = input('Vou odbre o numero que vc digitar: ')   

try:
    print(numero_string)
    numero_float = float(numero_string)
    print(numero_float)
    print(f'O dobro do {numero_string} é {numero_float * 2:.2f}')
except:
    print('O valor digitado não é um numero.')