# -------->> FORMATCAO DE STRING <<------------

# -------->>>>>>>>>>> EXEMPLO 1 <<<<<<<<<<<<<<------------
print('EXEMPLO 1 - STRING')
altura = 1.856
nome = 'Renan Menezes'
linha = f'{nome} tem tem {altura:.3f} de altura'
print(linha)
print()

# -------->>>>>>>>>>> EXEMPLO 2 <<<<<<<<<<<<<<------------
print('EXEMPLO 2 - FORMATANDO POR ARGUMENTO FUNCAO FORMAT')
variavel_a = 'aaa'
variavel_b = 'bbb'
variavel_c = 1.12345
variavel_string = 'a={} b={} c={:.2f}'
formato = variavel_string.format(variavel_a, variavel_b, variavel_c)
print(formato)
print()

# -------->>>>>>>>>>> EXEMPLO 3 -  UTILIZANDO INDICES <<<<<<<<<<<<<<-------------

# DENTRO DAS {} PODEMOS COLOCAR O INDICES DOS ARGUMENTOS DENTRO DA FUNCAO FORMAT
# DENTRO DA FUNCAO FORMAT PODEMOS TER UM ARGUMENTO NOMEADO
# OU PARAMETRO NOMEADO, NESTE CASO NAO PODEREMOS UTILIZAR O INDICE E SIM O NOME
print('EXEMPLO 3 - UTILIZANDO INDICES das strings')
variavel_a = 'aaa'
variavel_b = 'bbb'
variavel_c = 1.12345
variavel_strings= 'a={0} b={1} c={c:.2f}'
formato = variavel_strings.format(
    
    variavel_a, variavel_b, c=variavel_c
    
    )
print(formato)
print()

# -------->>>>>>>>>>> EXEMPLO 4 - INTERPOLACAO DE STRING <<<<<<<<<<<<<<-------------
# REGRAS INTERPOLCAO
# S      - STRING
# D ou I - INT
# F      - FLOAT
# X      - HEXADECIMAL
print('EXEMPLO 4 - INTERPOLACAO STRINGS')
nome_mercado = 'Piratininga'
valor_arroz = 10.56
variavel = 'No mercado %s o Arroz esta custando R$%.2f' % (nome_mercado,valor_arroz)

print(variavel)
print()

# -------->>>>>>>>>>> EXEMPLO 5 - FORMATACAO DE STRINGS <<<<<<<<<<<<<<-------------
# > - ESQUERDA
# < - DIRETIA
# ^ - CENTRO
# Sinal - + ou - 
# CONVERSION FLAGS - !r !s !a
print('EXEMPLO 5 - FORMATACAO POR POSICOES STRINGS')
variavel = 'ABC'
print(f'{variavel: >10}')  # ESQUERDA
print(f'{variavel: <10}.') # DIRETIA
print(f'{variavel: ^10}')  # CENTRO
print(f'{variavel:0>10}')  # ESQUERDA
print(f'{variavel:0<10}.') # DIRETIA
print(f'{variavel:0^10}')  # CENTRO
print()

# -------->>>>>>>>>>> EXEMPLO 6 - FORMATACAO DE STRINGS <<<<<<<<<<<<<<-------------
# FATEAMENTO [i:f:p]
# i = Inicio
# f = Final
# p = Passo, que é de quantos em quantos caracteres ele vai pular.
print('EXEMPLO 6 - FATEAMENTO DE STRINGS')

nome = 'Renan Bastos Cunha de Menezes'
fatiamento_0 = nome[:5]
fatiamento_1 = nome[0:5]
fatemaneto_2 = nome[0:len(nome):1]
fatemaneto_3 = nome[0:len(nome):2]
fatemaneto_4 = nome[0:len(nome):3]
print('Tamanho da String "nome": ', len(nome), ' - len(nome)')
print(fatiamento_0, ' - variavel[:5]')
print(fatiamento_1, ' - variavel[0:5]')
print(fatemaneto_2, ' - variavel[0:len(nome):1]')
print(fatemaneto_3, ' - variavel[0:len(nome):2]')
print(fatemaneto_4, ' - variavel[0:len(nome):3]')
print()

