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

pessoa = {
    'nome': 'Jesus Cristo',
    'sobrenome': 'Nazareno Filho do Deus Vivo',
    'idade': 33,
    'altura': 1.8
}

# --->> len - Quantidade de CHAVES
print(' --------------->>>>>> Exemplo len() <<<<<<---------------','\n')
print(len(pessoa),' chaves - ', pessoa, '\n')

# --->> keys - Retorna as CHAVES
print(' --------------->>>>>> Exemplo keys() <<<<<<---------------','\n')
print(pessoa.keys(), '\n')
# Podemos tranformar em lista para iterar e acessar.
print(list(pessoa.keys()), '\n')

# --->> values - Retorna as CHAVES
#iteravel com os valores.
print(' --------------->>>>>> Exemplo values() <<<<<<---------------','\n')
for valor in pessoa.values():
    print(valor)
print()

# Sem values iteravel com as chaves
for valor in pessoa:
    print(valor)
print()

# --->> items - Retorna as CHAVES
print(' --------------->>>>>> Exemplo items() <<<<<<---------------','\n')
# iteravel com CHAVE e VALOR.
for item in pessoa.items():
    print(item)
print()

# iteravel com CHAVE e VALOR.
for chave, valor in pessoa.items():
    print(chave, valor)
print()


