print('---------- Exemplo 1 Raise ---------- ','\n')
# Basicamente o raise retorna a Exceção.

def erro_divide_por_zero(p):
    if p == 0:
        raise ZeroDivisionError('>>>>>>>> Vc Esta Dividindo por Zero <<<<<<<<<')
    
def tipagem(p):
    if not isinstance(p, (float, int)):
        raise TypeError(
            f'{p} tem que ser um int ou um float '
        )

def divide (n, m):
    # Verifica Divisão por Zero
    erro_divide_por_zero(n)
    erro_divide_por_zero(m)

    # Verifica Tipagem
    tipagem(n)
    tipagem(m)

    return n / m

print(divide('kkk', 4))