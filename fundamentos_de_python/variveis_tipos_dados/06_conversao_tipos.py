# 6. CONVERSÃO DE TIPOS (TYPE CASTING)

"""
CONVERSÃO DE TIPOS EM PYTHON:
- int(): converte para inteiro
- float(): converte para decimal
- str(): converte para string
- bool(): converte para booleano
- list(), tuple(), set(): conversões entre coleções
"""

print("=== CONVERSÃO DE TIPOS ===")

# String para número
texto_numero = "123"
numero = int(texto_numero)
print(f"'{texto_numero}' convertido para int: {numero}")

# Número para string
idade = 25
idade_texto = str(idade)
print(f"{idade} convertido para string: '{idade_texto}'")

# Float para int (perde a parte decimal)
decimal = 3.14
inteiro = int(decimal)
print(f"{decimal} convertido para int: {inteiro}")

# Qualquer valor para boolean
print(f"bool(0): {bool(0)}")           # False
print(f"bool(1): {bool(1)}")           # True
print(f"bool(''): {bool('')}")         # False (string vazia)
print(f"bool('texto'): {bool('texto')}")  # True

# Conversões entre coleções
lista = [1, 2, 3, 4, 5]
tupla = tuple(lista)
conjunto = set(lista)
print(f"Lista para tupla: {tupla}")
print(f"Lista para set: {conjunto}")

# String para lista
frase = "Python"
lista_chars = list(frase)
print(f"String para lista: {lista_chars}")

# Tratamento de erros na conversão
try:
    numero_invalido = int("abc")
except ValueError as e:
    print(f"Erro na conversão: {e}")

# Conversões úteis
print(f"\nConversões úteis:")
print(f"String para float: {float('3.14')}")
print(f"Boolean para int: {int(True)}")  # True = 1, False = 0
print(f"Lista para string: {''.join(['a', 'b', 'c'])}")