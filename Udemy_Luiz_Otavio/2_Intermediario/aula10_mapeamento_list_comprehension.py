print('------------ > MAPEAMENTO List Comprehension < ------------', '\n')

print('>>>>>>>>>> Exemplo 1 - Empacotando uma lista com Comprehension <<<<<<<<<')
print('Reajustando o valor de preço em 5%', '\n')

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 30},
    {'nome': 'p3', 'preco': 40}
]

# Reajustando o valor de preço em 5%
novos_produtos = [
    {**produto, 'preco_novo': produto['preco'] * 1.05, 'preco_antigo': produto['preco'] }
    for produto in produtos
]

print(*novos_produtos,  sep='\n')
print('-----------------------------------------------------------------------------------------')
print()

# -------->>>>>> EXEMPLO 2 - FILTRANDO no MAPEAMETO DE DADOS e REAJUSTANDO VALOR com Comprehension <<<<<<<<<<<<<<------------

print('>>>>>>>>>> Exemplo 2 - FILTRANDO no MAPEAMETO DE DADOS e REAJUSTANDO VALOR com Comprehension <<<<<<<<<')
print('FILTRO (if produto["preco"] > 20)','\n')

print('OBS: Perceba que o produto "p1" não foi aplicado "novo_valor" e "antigo_valor"')
print('     Por causa do filtro  (if produto["preco"] > 20)','\n')

print('Porem perceba o produto "p1" mesmo não tendo o valor > 20 ')
print('ele veio na lista, ou seja "p1" não foi filtrado, somente o mapeamento foi.','\n')

print('Tudo que for aplicado a ESQUERDA do FOR será mapeamento')
print('E tudo que for aplicado a DIREITA do FOR será realmente FILTRADO','\n')

# Reajustando e FILTRANDO o valor. 
novos_produtos_mapeados = [
    {**produto, 'preco_novo': produto['preco'] * 1.05, 'preco_antigo': produto['preco'] }
    # Filtro Mapeamento
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(*novos_produtos_mapeados,  sep='\n')
print('-----------------------------------------------------------------------------------------')
print()

# -------->>>>>> EXEMPLO 3 - FILTRANDO os DADOS e REAJUSTANDO VALOR com Comprehension <<<<<<<<<<<<<<------------

print('>>>>>>>>>> Exemplo 3 - FILTRANDO os DADOS e REAJUSTANDO VALOR com Comprehension <<<<<<<<<<')
print('FILTRO (if produto["preco"] > 20)','\n')

print('OBS: Perceba que o produto "p1" nem sequer apareceu no print')
print('     Por causa do filtro  (if produto["preco"] > 20)','\n')

# Reajustando e FILTRANDO o valor. 
novos_produtos_filtrados = [
    {**produto, 'preco_novo': produto['preco'] * 1.05, 'preco_antigo': produto['preco'] }
    # Filtro Mapeamento
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    # Filtro de Dados
    if produto['preco'] > 20
]

print(*novos_produtos_filtrados,  sep='\n')
