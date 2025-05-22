# Crie Funcoes que duplicam, triplicam, e quadruplicam

def criar_multiplicador(multiplicador):

    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)

print(duplicar(2), 'Duplicou')
print(triplicar(2), 'Triplicou')
print(quadriplicar(2), 'Quadriplicou')