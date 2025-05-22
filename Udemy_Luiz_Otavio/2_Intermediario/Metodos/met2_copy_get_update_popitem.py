# Metodos uteis dos DICIONARIOS.
# len - quantas chaves.
# keys - iteravel com as chaves.
# values - iteravel com os valores.
# items - iteravel com chaves e valores.
# setdefault - adiciona valor se a chave não existe.
# copy - retorna uma copia rasa (shallow copy).
# get - obtem uma chave.
# pop - Apaga o ultimo item adicionado.
# update - Atualiza um dicionario com outro.
import copy

pessoa = {
    'nome': 'Jesus Cristo',
    'sobrenome': 'Nazareno Filho do Deus Vivo',
    'idade': 33,
    'altura': 1.8
}

# --->> copy - retorna uma copia rasa (shallow copy).
print(' --------------->>>>>> Exemplo copy() Shallow "Rasa" <<<<<<---------------','\n')

filho_deus_vivo = pessoa.copy()

print(filho_deus_vivo, '\n')


# --->> deepcopy - retorna uma copia Profunda
print(' --------------->>>>>> Exemplo deepcopy() Profundo <<<<<<---------------','\n')

senhor_e_salvador = copy.deepcopy(pessoa)

print(senhor_e_salvador, '\n')

# --->> get - obtem o valor de uma chave.
print(' --------------->>>>>> Exemplo get() <<<<<<---------------','\n')

exemplo_get = pessoa.get('nome')

print(exemplo_get, '\n')

# --->> pop - Apaga o ultimo item adicionado.
print(' --------------->>>>>> Exemplo pop() <<<<<<---------------','\n')

exemplo_pop = pessoa.pop('altura')

print(exemplo_pop, '\n')
print(pessoa, '\n')

# --->> popitem - Remove a ultima chave do DICIONARIO
print(' --------------->>>>>> Exemplo popitem() <<<<<<---------------','\n')

exemplo_popitem = pessoa.popitem()

print('Chave Deletada: ', exemplo_popitem, '\n')
print(pessoa, '\n')

# --->> update - Atualiza valor docionario
print(' --------------->>>>>> Exemplo update() <<<<<<---------------','\n')

pessoa.update(sobrenome='Meu Senhor e Meu Resgate')

print(pessoa, '\n')

