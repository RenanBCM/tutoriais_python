# Modularização - Entendendo os seus próprios módulos Python
 # O primeiro módulo executado chama-se __main__
 # O python conhece a pasta onde o __main__ está e as pastas abaixo dele.
 # Ele não reconhece pastas e módulos acima do __main__ por padrão
 # O python conhece todos os módulos e pacotes presentes nos caminhos de sys.path
import sys
import Aula17_2_Estenção

print('Este módulo se chama', __name__)

print(Aula17_2_Estenção.teste())

# Lista todos os caminhos das bibliotecas
print(*sys.path, sep='\n')
