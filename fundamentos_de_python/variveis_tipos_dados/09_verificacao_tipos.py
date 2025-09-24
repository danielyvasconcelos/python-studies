# 9. VERIFICAÇÃO DE TIPOS E VALORES

"""
VERIFICAÇÃO EM PYTHON:
- type(): retorna o tipo exato da variável
- isinstance(): verifica se é instância de um tipo (recomendado)
- hasattr(): verifica se objeto tem determinado atributo
- callable(): verifica se objeto é chamável (função)
- dir(): lista atributos e métodos disponíveis
"""

print("=== VERIFICAÇÕES ===")

numero = 42
texto = "Python"
lista = [1, 2, 3]

# Verificar tipo
print(f"Tipo de {numero}: {type(numero)}")
print(f"É inteiro? {isinstance(numero, int)}")
print(f"É string? {isinstance(texto, str)}")

# isinstance é melhor que type para verificações
print(f"\nComparação type vs isinstance:")
print(f"type(numero) == int: {type(numero) == int}")
print(f"isinstance(numero, int): {isinstance(numero, int)}")

# Verificar múltiplos tipos
print(f"É int ou float? {isinstance(numero, (int, float))}")

# Verificar se variável existe
if 'numero' in locals():
    print("Variável 'numero' existe no escopo local")

if 'numero' in globals():
    print("Variável 'numero' existe no escopo global")

# Verificar valor (truthiness)
valores = [0, 1, "", "texto", [], [1], {}, {"a": 1}, None, True, False]
print(f"\nVerificação de valores (truthiness):")
for valor in valores:
    print(f"{repr(valor):>10} é {'True' if valor else 'False'}")

# Verificar atributos e métodos
print(f"\nVerificações avançadas:")
print(f"Lista tem método 'append'? {hasattr(lista, 'append')}")
print(f"Número é chamável? {callable(numero)}")
print(f"Print é chamável? {callable(print)}")

# Verificar se é iterável
def eh_iteravel(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

print(f"String é iterável? {eh_iteravel(texto)}")
print(f"Número é iterável? {eh_iteravel(numero)}")

# Métodos úteis de verificação
print(f"\nMétodos de string:")
print(f"'123'.isdigit(): {'123'.isdigit()}")
print(f"'abc'.isalpha(): {'abc'.isalpha()}")
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")
print(f"'   '.isspace(): {'   '.isspace()}")