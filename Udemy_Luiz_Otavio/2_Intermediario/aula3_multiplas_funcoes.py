# -------->>>>>>>>>>> EXEMPLO 1 - Multiplas Funcoes <<<<<<<<<<<<<<------------

print('-------->>>>>>>>>>> Exemplo 1 - Multiplas Funções <<<<<<<<<<<<<<------------', '\n')

def saudacao(msg, nome):
    return f'{msg}, {nome}' 

# Funcao recebe uma Funcao
def executa(funcao, *args):
    return funcao(*args)

executa_variavel = executa(saudacao,'Bom dia','Jesus Cristo é Meu Senhor')
print(executa_variavel, '\n')

# -------->>>>>>>>>>> EXEMPLO 2 - Closure <<<<<<<<<<<<<<------------

print('-------->>>>>>>>>>> Exemplo 2 - Closure <<<<<<<<<<<<<<------------', '\n')

def criar_saudacao(saudacao, nome):

    def saudar():
        return f'{saudacao}, {nome}'
    return saudar

bom_dia = criar_saudacao('Bom dia', 'Cristo Jesus')
boa_noite = criar_saudacao('Boa Noite', 'Toda Gloria Para Deus')

print(bom_dia())   # O "Closure" temos que colocar os parenteses nessas variaveis para rodar o print
print(boa_noite()) # <<------ Closure