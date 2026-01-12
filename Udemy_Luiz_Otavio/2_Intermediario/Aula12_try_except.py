
print('---------- Exemplo 1 Try Except - BASICO ---------- ','\n')

a = 10
b = 0
c = 20

# Erro Divisão por ZERO
try:
    c = a / b
except:
    print('Dividiu por Zero.','\n')

# Não declarou variavel do calculo
try:
    a / e
except:
    print('Não declarou variavel do calculo','\n')

print('---------- Exemplo 2 Try Except - CLASSES ---------- ','\n')

# Erro Divisão por ZERO
try:
    f = a / c

    # Erro Classe Exception
    print(a[3])

    # Erro Variavel não declarada.
    erro = a / g

except ZeroDivisionError:
    print('Dividiu por Zero.','\n')
except NameError:
    print('Variavel não declarada.','\n')
except Exception:
    print('Classe Exception -  Trata Todos os Erros','\n')

print('---------- Exemplo 3 Try Except - 2 CLASSES ou MAIS ---------- ','\n')

# Erro Divisão por ZERO
try:
    # Erro Index
    print('Linha 1'[1000])

except (TypeError, IndexError):
    print('IndexError - Indice Não Existe','\n')

print('CONTINUAR')

