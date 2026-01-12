# Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes
import sys
print(sys.platform)

# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo
from sys import exit, platform

print(platform)

# má prática - from nome_modulo import *
from sys import exit as ex
from sys import platform as pf

print(platform)