# 2. TIPOS BÁSICOS DE VARIÁVEIS

"""
TIPOS PRIMITIVOS EM PYTHON:
- int: números inteiros
- float: números decimais
- str: texto/string
- bool: valores lógicos (True/False)
- complex: números complexos
"""

print("=== TIPOS BÁSICOS ===")

# NÚMEROS INTEIROS (int)
idade = 30
quantidade = -5
numero_grande = 1000000
print(f"Inteiro: {idade}, tipo: {type(idade)}")

# NÚMEROS DECIMAIS (float)
altura = 1.75
preco = 29.99
temperatura = -10.5
print(f"Float: {altura}, tipo: {type(altura)}")

# TEXTO (str - string)
nome = "Maria"
sobrenome = 'Silva'  # Aspas simples ou duplas
frase = """Texto com
múltiplas linhas"""
print(f"String: {nome}, tipo: {type(nome)}")
print(f"String: {sobrenome}, tipo: {type(sobrenome)}")
print(f"String: {frase}, tipo: {type(frase)}")

# BOOLEANO (bool)
ativo = True
logado = False
print(f"Boolean: {ativo}, tipo: {type(ativo)}")

# NÚMERO COMPLEXO (complex)
numero_complexo = 3 + 4j
print(f"Complex: {numero_complexo}, tipo: {type(numero_complexo)}")

# Verificação de tipos
print(f"\nVerificações:")
print(f"É inteiro? {isinstance(idade, int)}")
print(f"É float? {isinstance(altura, float)}")
print(f"É string? {isinstance(nome, str)}")
print(f"É boolean? {isinstance(ativo, bool)}")