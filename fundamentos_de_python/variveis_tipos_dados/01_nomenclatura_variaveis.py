# 1. REGRAS PARA NOMES DE VARIÁVEIS

"""
NOMENCLATURA DE VARIÁVEIS EM PYTHON:
- Devem começar com letra ou underscore (_)
- Podem conter letras, números e underscores
- São case-sensitive (nome ≠ Nome)
- Não podem usar palavras reservadas do Python
- Convenção: snake_case para variáveis e funções
"""

# ✅ VÁLIDOS:
nome = "João"
idade = 25
_privada = "variável privada"
numero1 = 10
minha_variavel = "snake_case"
minhaVariavel = "camelCase"

# ❌ INVÁLIDOS (descomente para ver os erros):
# 1nome = "erro"        # Não pode começar com número
# minha-variavel = "erro"  # Não pode usar hífen
# class = "erro"        # Não pode usar palavras reservadas
# minha variavel = "erro"  # Não pode ter espaços

print("=== NOMES DE VARIÁVEIS ===")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Variável privada: {_privada}")

# Convenções importantes:
# - Use nomes descritivos
# - snake_case para variáveis e funções
# - MAIÚSCULAS para constantes
# - _variavel para indicar uso interno
# - __variavel para name mangling (muito privada)