# -------->>>>>>>>>>> PRIMEIRO DIGITO <<<<<<<<<<<<<<------------

# Colete a soma dos 9 primeiros digitos do CPF.
# Multiplicando cada um dos valores por uma contagem regressiva começando de 10
# CPF: 294.737.300-63
#
# Calculo:
# Exemplo 294.737.300-63 (294737300)
#
#   10   9   8   7   6   5   4  3  2  (Valores por contagem regressiva começando de 10)
#    2   9   4   7   3   7   3  0  0  (9 Primeiros Digitos CPF)
#   20  81  32  49  18  35  12  0  0  (Resultado da Multiplicacao)
#
# Somar todos os resultados: 247
# 20 + 81 + 32 + 49 + 18 + 35 + 12 + 0 + 0 = 247
# 
# Multiplicar a Soma por 10
# 247 * 10 = 2470
#
# O resto da conta anterior por 11
# 2470 % 11 = 6
#
# Se o resultado do resto for Maior que 9 entao resultado = 0
# contrario disso e o resultado do resto
# Resto = 6
#
# O primeiro Digito do CPF = 6
# Tudo ok

print('-------->>>>>>>>>>>  Gerando o PRIMEIRO DIGITO do CPF <<<<<<<<<<<<<<------------ ', '\n')

cpf = '29473730063'
nove_digitos = cpf[:9]

print('9 primeiros numeros CPF: ',nove_digitos, '\n')

print('Gerando Primeiro Digito: ', '\n')

contador_regressivo_dg1 = 10

soma_resultados_1dg = 0
for digito_1dg in nove_digitos:
    resultado_1dg = int(digito_1dg) * contador_regressivo_dg1
    soma_resultados_1dg += int(digito_1dg) * contador_regressivo_dg1
    print(digito_1dg, contador_regressivo_dg1, ' = ', resultado_1dg)
    contador_regressivo_dg1 -= 1

print('Soma dos Resultados: ', soma_resultados_1dg)

resto_1dg = ((soma_resultados_1dg * 10) % 11)
print('Resto: ', resto_1dg)

primeiro_digito = 0 if resto_1dg > 9 else resto_1dg
print('Primeiro Digito do CPF: ', primeiro_digito, '\n')

# -------->>>>>>>>>>> SEGUNDO DIGITO <<<<<<<<<<<<<<------------

# Colete a soma dos 9 primeiros digitos do CPF + o PRIMEIRO DIGITO.
# Multiplicando cada um dos valores por uma contagem regressiva começando de 11
# CPF: 294.737.300-63
#
# Calculo:
# Exemplo 294.737.300-63 (294737300)
#
#   11  10   9   8   7   6   5  4  3   2  (Valores por contagem regressiva começando de 11)
#    2   9   4   7   3   7   3  0  0   6  (9 Primeiros Digitos CPF)
#   22  90  36  56  21  42  15  0  0  12  (Resultado da Multiplicacao)
#
# Somar todos os resultados: 247
# 20 + 81 + 32 + 49 + 18 + 35 + 12 + 0 + 0 = 294
# 
# Multiplicar a Soma por 10
# 259 * 10 = 2940
#
# O resto da conta anterior por 11
# 2940 % 11 = 3
#
# Se o resultado do resto for Maior que 9 entao resultado = 0
# contrario disso e o resultado do resto
# Resto = 3
#
# O SEGUNDO Digito do CPF = 3
# Tudo ok

print(' -------->>>>>>>>>>> Gerando o SEGUNDO DIGITO do CPF <<<<<<<<<<<<<<------------ ', '\n')

dez_digitos = nove_digitos + str(primeiro_digito)

print('10 primeiros numeros CPF: ',dez_digitos, '\n')

print('Calculo Segundo Digito: ', '\n')

contador_regressivo_dg2 = 11

soma_resultados_2dg = 0
for digito_2dg in dez_digitos:
    resultado_2dg = int(digito_2dg) * contador_regressivo_dg2
    soma_resultados_2dg += int(digito_2dg) * contador_regressivo_dg2
    print(digito_2dg, contador_regressivo_dg2, ' = ', resultado_2dg)
    contador_regressivo_dg2 -= 1

print('Soma dos Resultados: ', soma_resultados_2dg)

resto_2dg = ((soma_resultados_2dg * 10) % 11)
print('Resto: ', resto_2dg)

segundo_digito = 0 if resto_2dg > 9 else resto_2dg
print('Segundo Digito do CPF: ', segundo_digito, '\n')

# -------->>>>>>>>>>> CPF COMPLETO <<<<<<<<<<<<<<------------

print(' -------->>>>>>>>>>> CPF COMPLETO <<<<<<<<<<<<<<------------ ', '\n')

print(nove_digitos,primeiro_digito,segundo_digito)