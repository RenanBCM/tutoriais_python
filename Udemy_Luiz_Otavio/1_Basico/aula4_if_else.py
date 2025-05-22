# -------->>>>>>>>>>> EXEMPLO 1 <<<<<<<<<<<<<<------------
entrada = input('Digite [E]ntrada ou [S]saida: ')
senha_digitada = input('senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and (senha_permitida == senha_digitada):
   print('Entrar')
else:
   print('Sair')

# -------->>>>>>>>>>> EXEMPLO 2 <<<<<<<<<<<<<<------------
entrada = input('Voce quer "entrar" ou "sair" ?')

if entrada == 'entrar':
    print('vc entrou no sistema')
elif entrada == 'sair':
    print('vc saiu do sistema')
else:
    print('vc nao digitou nem "entrar" ou "sair".')



