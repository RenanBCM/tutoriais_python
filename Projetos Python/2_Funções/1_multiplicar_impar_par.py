# Exercicio Com Funções

# Crie uma função que multiplica todos os argumentos não nomeados.
# Retorne o TOTAL para uma variavel e mostre o valor da variavel.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    
    return total

multiplicacao = multiplicar(1,2,3,4,5)

print(multiplicacao, '\n')

# Crie uma função que retorna se o numero é PAR ou IMPAR.

print('Exercico 2 - Retorna se o numero é PAR ou IMPAR')

def impar_par(numero_par_impar):
    if numero_par_impar % 2 == 0:
       return print(numero_par_impar, ' é um numero PAR')
    else:
       return print(numero_par_impar, ' é um numero IMPAR')

impar_par(3)
impar_par(4)
impar_par(8)
