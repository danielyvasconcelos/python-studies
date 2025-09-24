# 8. VARIÁVEIS ESPECIAIS

"""
VARIÁVEIS ESPECIAIS EM PYTHON:
- None: representa ausência de valor
- _variavel: convenção para variável "privada"
- __variavel: name mangling (muito privada)
- CONSTANTE: convenção para constantes (maiúsculas)
- __name__: nome do módulo atual
- __file__: caminho do arquivo atual
"""

print("=== VARIÁVEIS ESPECIAIS ===")

# None - representa ausência de valor
valor_nulo = None
print(f"Valor nulo: {valor_nulo}, tipo: {type(valor_nulo)}")

# Variáveis com underscore (convenções) pq?
# _ indica que é para uso interno (convenção)
_variavel_privada = "Por convenção, é privada"
# __ ativa o name mangling (Python modifica o nome)
__variavel_muito_privada = "Muito privada"
# MAIÚSCULAS indicam constantes (convenção)
CONSTANTE = "Por convenção, é uma constante"

print(f"Constante: {CONSTANTE}")

# Variáveis especiais do Python
print(f"\nVariáveis especiais do sistema:")
print(f"Nome do módulo: {__name__}")
print(f"Arquivo atual: {__file__}")

# Exemplo de uso do None
def funcao_sem_retorno():
    print("Esta função não retorna nada explicitamente")

resultado = funcao_sem_retorno()
print(f"Resultado da função: {resultado}")  # None

# Verificando se uma variável é None
if resultado is None:
    print("A função retornou None")

# Constantes comuns
PI = 3.14159
VELOCIDADE_LUZ = 299792458  # m/s
GRAVIDADE = 9.81  # m/s²

print(f"\nConstantes:")
print(f"PI: {PI}")
print(f"Velocidade da luz: {VELOCIDADE_LUZ} m/s")
print(f"Gravidade: {GRAVIDADE} m/s²")

# Variável especial para descarte
_, segundo, _ = (1, 2, 3)  # Descarta primeiro e terceiro valores
print(f"Segundo valor: {segundo}")