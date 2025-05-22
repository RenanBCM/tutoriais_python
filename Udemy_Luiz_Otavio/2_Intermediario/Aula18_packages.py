from sys import path
from packages_exemplos.modulo_packages import soma_do_modulo   

print(__name__)         # Utilizado para saber se o arquivo executado é o main
print(*path, sep='\n')

print(soma_do_modulo(4, 5))