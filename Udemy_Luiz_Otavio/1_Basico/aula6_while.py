# -------->>>>>>>>>>> EXEMPLO 1 <<<<<<<<<<<<<<------------

print('EXEMPLO 1 - WHILE')

contador = 0

while contador <= 15:
      print('Contador: ', contador)
      contador += 1 # (+= 1) = (contador + 1)

print('ACABOU EXEMPLO 1')
print()

# -------->>>>>>>>>>> EXEMPLO 2 <<<<<<<<<<<<<<------------

print('EXEMPLO 2 - WHILE DENTRO DE OUTRO WHILE')

qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
      coluna = 1

      while coluna <= qtd_colunas:
            print(f'{linha = }, {coluna = }')
            coluna += 1

      linha += 1

print('ACABOU EXEMPLO 2 - WHILE DENTRO DE OUTRO WHILE')
print()

# -------->>>>>>>>>>> EXEMPLO 3 <<<<<<<<<<<<<<------------

print('EXEMPLO 3 - WHILE ITERANDO UMA STRING')

frase = 'Porque a palavra da cruz é loucura para os que perecem' \
' mas para nós, que somos salvos, é o poder de Deus.' \
' - 1 Coríntios 18'

i = 0
qtd_apareceu_mais_vezes = 0

while i < len(frase):
      letra_atual = frase[i]
      qtd_apareceu_mais_vezes_atual = frase.count(letra_atual)

      if letra_atual == ' ':
         i += 1
         continue 

      if qtd_apareceu_mais_vezes < qtd_apareceu_mais_vezes_atual:
         
         qtd_apareceu_mais_vezes = qtd_apareceu_mais_vezes_atual
         letra_apareceu_mais_vezes = letra_atual

      print(letra_atual, qtd_apareceu_mais_vezes_atual)
      i += 1

print('A letra que apareceu mais vezes: ', letra_apareceu_mais_vezes)
print('ACABOU EXEMPLO 3 - WHILE ITERANDO UMA STRING')