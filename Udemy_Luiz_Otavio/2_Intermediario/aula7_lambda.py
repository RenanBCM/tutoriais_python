# -------->>>>>>>>>>> EXEMPLO 1 - lambda <<<<<<<<<<<<<<------------

print('Exemplo 1 lambda','\n')

def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

# Fazendo a função Executa() com LAMBDA
print(
    executa( lambda x, y: x + y, 2, 3 ),  # 3 funções iguais - lambda
    executa(soma, 2, 3),                  # 3 funções iguais
    soma(2, 3),                           # 3 funções iguais
    '\n'
)

# Fazendo a função soma() com LAMBDA
print(
    executa( 
        lambda *args: sum(args),
        1, 2, 3, 4, 5, 6, 7
          )
)

