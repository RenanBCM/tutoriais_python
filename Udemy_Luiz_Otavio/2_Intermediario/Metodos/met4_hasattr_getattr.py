string = 'luiz'

# -------->>>>>>>>>>> EXEMPLO 1 - hasattr() <<<<<<<<<<<<<<------------

# Server para consultar se um metodo existe dentro de um objeto
# Se existir o metodo retorna TRUE.

if hasattr(string, 'upper'):
    print('Existe sim o Metodo"UPPER" dentro do objeto STRING.', '\n')

# -------->>>>>>>>>>> EXEMPLO 2 - getattr() <<<<<<<<<<<<<<------------

# Server para consultar exibir a descrição de um metodo de um objeto.
# Se existir o metodo retorna com a descrição.

if hasattr(string, 'upper'):
    print('Existe sim o Metodo"UPPER" dentro do objeto STRING.', '\n')
    print( getattr(string, 'upper'), '\n')
