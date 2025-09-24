# OPERADORES EM PYTHON - GUIA COMPLETO MODULARIZADO

"""
OPERADORES EM PYTHON:
São símbolos especiais que realizam operações em operandos (valores/variáveis).
Python possui diversos tipos de operadores para diferentes finalidades.

Este arquivo lista todos os módulos de estudo sobre operadores.
"""

print("=" * 60)
print("OPERADORES EM PYTHON - GUIA COMPLETO PARA ESTUDOS")
print("=" * 60)

# Lista dos arquivos para executar
arquivos_estudo = [
    "operadores_aritmeticos.py",
    "operadores_de_comparacao.py", 
    "operador_logico_AND.py",
    "operador_logico_OR.py",
    "operador_logico_NOT.py",
    "operadores_de_atribuicao.py",
    "operadores_de_identidade.py",
    "operadores_de_pertencimento.py"
]

print("\n📋 ARQUIVOS DISPONÍVEIS PARA ESTUDO:")
for i, arquivo in enumerate(arquivos_estudo, 1):
    nome_limpo = arquivo.replace('.py', '').replace('_', ' ').title()
    print(f"{i:2d}. {arquivo:<35} - {nome_limpo}")

print("\n" + "=" * 60)
print("📚 TIPOS DE OPERADORES ABORDADOS:")
print("=" * 60)

tipos_operadores = [
    ("🔢 Aritméticos", "Operações matemáticas (+, -, *, /, //, %, **)"),
    ("⚖️  Comparação", "Comparar valores (==, !=, <, >, <=, >=)"),
    ("🔗 Lógicos", "Operações lógicas (and, or, not)"),
    ("📝 Atribuição", "Atribuir valores (=, +=, -=, *=, /=, etc.)"),
    ("🆔 Identidade", "Comparar objetos (is, is not)"),
    ("📦 Pertencimento", "Verificar presença (in, not in)")
]

for tipo, descricao in tipos_operadores:
    print(f"{tipo:<15} - {descricao}")

print("\n" + "=" * 60)
print("🎯 PRECEDÊNCIA DOS OPERADORES (maior para menor):")
print("=" * 60)

precedencia = [
    "1. ** (potenciação)",
    "2. +x, -x, ~x (unários: positivo, negativo, NOT bit a bit)",
    "3. *, /, //, % (multiplicação, divisões, módulo)",
    "4. +, - (adição, subtração)",
    "5. <<, >> (shifts bit a bit)",
    "6. & (AND bit a bit)",
    "7. ^ (XOR bit a bit)",
    "8. | (OR bit a bit)",
    "9. ==, !=, <, >, <=, >=, is, is not, in, not in (comparações)",
    "10. not (NOT lógico)",
    "11. and (AND lógico)",
    "12. or (OR lógico)",
    "13. = (atribuição)"
]

for item in precedencia:
    print(f"   {item}")

print("\n" + "=" * 60)
print("💡 COMO USAR ESTE MATERIAL:")
print("=" * 60)

instrucoes = [
    "1. Execute cada arquivo individualmente para estudar tópicos específicos",
    "2. Comece pelos operadores básicos (aritméticos e comparação)",
    "3. Pratique modificando os valores nos exemplos",
    "4. Leia os comentários para entender conceitos importantes",
    "5. Use como referência durante desenvolvimento"
]

for instrucao in instrucoes:
    print(f"   {instrucao}")

print("\n" + "=" * 60)
print("🚀 EXEMPLOS RÁPIDOS:")
print("=" * 60)

print("# Aritméticos")
print("10 + 5 = 15")
print("10 ** 2 = 100")

print("\n# Comparação")
print("10 > 5 = True")
print("'Python' == 'Python' = True")

print("\n# Lógicos")
print("True and False = False")
print("True or False = True")
print("not True = False")

print("\n# Atribuição")
print("x = 10")
print("x += 5  # x = 15")

print("\n# Identidade")
print("a = [1, 2]; b = [1, 2]")
print("a == b = True (mesmo conteúdo)")
print("a is b = False (objetos diferentes)")

print("\n# Pertencimento")
print("'Python' in 'Python é ótimo' = True")
print("5 in [1, 2, 3, 4, 5] = True")

print("\n" + "=" * 60)
print("📖 PARA EXECUTAR:")
print("=" * 60)
print("python operadores_aritmeticos.py")
print("python operadores_de_comparacao.py")
print("python operador_logico_AND.py")
print("# ... e assim por diante")

print("\n" + "=" * 60)
print("🎉 BOM ESTUDO!")
print("=" * 60)