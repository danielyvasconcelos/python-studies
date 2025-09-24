# 4. ATRIBUIÇÃO DE VARIÁVEIS

"""
FORMAS DE ATRIBUIÇÃO EM PYTHON:
- Atribuição simples: x = 10
- Atribuição múltipla: a, b, c = 1, 2, 3
- Atribuição com mesmo valor: x = y = z = 100
- Troca de valores: a, b = b, a
"""

print("=== ATRIBUIÇÃO ===")

# Atribuição simples
x = 10
print(f"x = {x}")

# Atribuição múltipla
a, b, c = 1, 2, 3
print(f"a={a}, b={b}, c={c}")

# Atribuição com mesmo valor
x = y = z = 100
print(f"x={x}, y={y}, z={z}")

# Troca de valores
a, b = 5, 10
print(f"Antes: a={a}, b={b}")
a, b = b, a  # Troca os valores
print(f"Depois: a={a}, b={b}")

# Atribuição com desempacotamento
lista = [1, 2, 3, 4, 5]
primeiro, segundo, *resto = lista
print(f"Primeiro: {primeiro}, Segundo: {segundo}, Resto: {resto}")

# Atribuição condicional (operador ternário)
idade = 20
status = "maior" if idade >= 18 else "menor"
print(f"Status: {status}")

# Operadores de atribuição compostos
numero = 10
numero += 5  # numero = numero + 5
print(f"Após +=: {numero}")
numero *= 2  # numero = numero * 2
print(f"Após *=: {numero}")