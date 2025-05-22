# -------->>>>>>>>>>> EXEMPLO 1 - VARIAVEIS E SEUS TIPOS <<<<<<<<<<<<<<------------

nome_completo = 'Renan Menezes'  # Variavel string
idade = 31                       # Variavel int
maior_idade = idade >= 18        # Variavel bool

print('EXEMPLO 1 - VARIAVEIS')
print('Maior de idade ? ', maior_idade)
print('nome_completo ', type(nome_completo))
print('maior_idade   ', type(maior_idade))
print('Nome: ', nome_completo, ', Idade: ', idade, ', maior_idade: ',maior_idade)
print()

# -------->>>>>>>>>>> EXEPLO 2 - CONSTANTES <<<<<<<<<<<<<<------------

# CONTANTES SAO VARIVEIS QUE O VALOR ATRIBUIDO A ELA NAO PODER SER ALTERADO.
# EM OUTRAS LINGUAGENS AS CONSTANTES EXISTEM, POREM EM PYTHON NAO TEMOS.
# POR UTILIZAMOS COMO CONVENCAO UTILIZAR VARIAVEIS COM LETRAS MAIUSCULAS PARA CONTANTES.

VALOCIDADE_RADAR_1 = 60
VELOCIDADE_RADAR_2 = 90

print('EXEMPLO 2 - CONSTANTES')
print('Bem Vindo a Consulta de Multas ONLINE:')
velocidade_motorista_trecho_1 = int(input('Digite qual velocidade passou no Radar 1: '))
velocidade_motorista_trecho_2 = int(input('Digite qual velocidade passou no Radar 2: '))

if (velocidade_motorista_trecho_1 > VALOCIDADE_RADAR_1):
   print('Senhor motorista')
   print(f'O radar 1 te multou pois sua velocidade foi de {velocidade_motorista_trecho_1}, e ultrapassou o limite de {VALOCIDADE_RADAR_1}')
   if (velocidade_motorista_trecho_2 > VELOCIDADE_RADAR_2):
      print(f'O radar 2 te multou pois sua velocidade foi de {velocidade_motorista_trecho_2}, e ultrapassou o limite de {VELOCIDADE_RADAR_2}')
   print('Pague suas multas na data certa')
   print()
else:
   print('Parabens o senhor nao tomou multas.')
   print()



