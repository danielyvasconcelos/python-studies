# 7. OPERAÇÕES COM VARIÁVEIS

"""
OPERAÇÕES EM PYTHON:
- Aritméticas: +, -, *, /, //, %, **
- Comparação: ==, !=, <, >, <=, >=
- Lógicas: and, or, not
- Atribuição: =, +=, -=, *=, /=
- Identidade: is, is not
- Pertencimento: in, not in
"""

print("=== OPERAÇÕES ===")

# Operações matemáticas
a = 10
b = 3
print(f"Soma: {a} + {b} = {a + b}")
print(f"Subtração: {a} - {b} = {a - b}")
print(f"Multiplicação: {a} * {b} = {a * b}")
print(f"Divisão: {a} / {b} = {a / b}")
print(f"Divisão inteira: {a} // {b} = {a // b}")
print(f"Resto: {a} % {b} = {a % b}")
print(f"Potência: {a} ** {b} = {a ** b}")

# Operações com strings
nome = "João"
sobrenome = "Silva"
nome_completo = nome + " " + sobrenome  # Concatenação
print(f"Nome completo: {nome_completo}")
print(f"Nome repetido: {nome * 3}")

# Operações de comparação
x, y = 5, 10
print(f"\nComparações:")
print(f"{x} == {y}: {x == y}")
print(f"{x} != {y}: {x != y}")
print(f"{x} < {y}: {x < y}")
print(f"{x} > {y}: {x > y}")

# Operações lógicas
print(f"\nOperações lógicas:")
print(f"True and False: {True and False}")
print(f"True or False: {True or False}")
print(f"not True: {not True}")

# Operadores de identidade
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1
print(f"\nIdentidade:")
print(f"lista1 is lista2: {lista1 is lista2}")  # False (objetos diferentes)
print(f"lista1 is lista3: {lista1 is lista3}")  # True (mesmo objeto)
print(f"lista1 == lista2: {lista1 == lista2}")  # True (mesmo conteúdo)

# Operadores de pertencimento
frutas = ["maçã", "banana", "laranja"]
print(f"\nPertencimento:")
print(f"'banana' in frutas: {'banana' in frutas}")
print(f"'uva' not in frutas: {'uva' not in frutas}")