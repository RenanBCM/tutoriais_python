# -------->>>>>>>>>>> EXEMPLO 1 - Com Argumento Nomeado e Não Nomeado <<<<<<<<<<<<<<------------

print('-------->>>>>>>>>>> Exemplo 1 - Funções Com Return <<<<<<<<<<<<<<------------', '\n')

def soma(x, y):
    if x > 10:
        return x + y
    
    return x * y

soma1 = soma(2, 14)

print(soma1, '\n')

# -------->>>>>>>>>>> EXEMPLO 2 - *args <<<<<<<<<<<<<<------------

print('------->>>>>>>>>>> Exemplo 2 - *args <<<<<<<<<<<<<<------------', '\n')

def multiplicacao(*args):

    total = 0

    for numero in args:
        total = total + numero
        print('argumento: ', numero)
        print('Somas Argumentos: ', total)
    return total

# Com *args posso colocar a quantidade argumentos que eu quiser ao chamar a funcao
print('Chamada 1 - multiplicacao(2,3,4)', '\n')
chamada_1 = multiplicacao(2,3,4)
print(chamada_1, '\n')

print('Chamada 2 - multiplicacao(7,7,7)', '\n')
chamada_2 = multiplicacao(7,7,7)
print(chamada_2, '\n')


