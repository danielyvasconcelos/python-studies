# 11. EXEMPLOS PRÁTICOS

"""
EXEMPLOS PRÁTICOS COM VARIÁVEIS:
- Calculadora simples
- Sistema de pontuação
- Contador de caracteres
- Gerenciador de estoque
- Calculadora de IMC
"""

print("=== EXEMPLOS PRÁTICOS ===")

# Calculadora simples
print("--- Calculadora ---")
num1 = 10
num2 = 5
operacao = "+"

if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2 if num2 != 0 else "Erro: divisão por zero"

print(f"{num1} {operacao} {num2} = {resultado}")

# Sistema de pontuação
print("\n--- Sistema de Pontuação ---")
pontuacao = 85
if pontuacao >= 90:
    conceito = "A"
elif pontuacao >= 80:
    conceito = "B"
elif pontuacao >= 70:
    conceito = "C"
else:
    conceito = "D"

print(f"Pontuação: {pontuacao} - Conceito: {conceito}")

# Contador de caracteres
print("\n--- Contador de Caracteres ---")
frase = "Python é incrível!"
total_caracteres = len(frase)
sem_espacos = len(frase.replace(" ", ""))
palavras = len(frase.split())

print(f"Frase: '{frase}'")
print(f"Total de caracteres: {total_caracteres}")
print(f"Caracteres sem espaços: {sem_espacos}")
print(f"Número de palavras: {palavras}")

# Gerenciador de estoque
print("\n--- Gerenciador de Estoque ---")
produto_nome = "Notebook"
quantidade_estoque = 15
preco_unitario = 2500.00
estoque_minimo = 5

valor_total_estoque = quantidade_estoque * preco_unitario
precisa_repor = quantidade_estoque <= estoque_minimo

print(f"Produto: {produto_nome}")
print(f"Quantidade em estoque: {quantidade_estoque}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Valor total do estoque: R$ {valor_total_estoque:.2f}")
print(f"Precisa repor estoque: {'Sim' if precisa_repor else 'Não'}")

# Calculadora de IMC
print("\n--- Calculadora de IMC ---")
peso = 70.5  # kg
altura = 1.75  # metros

imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")

# Sistema de desconto
print("\n--- Sistema de Desconto ---")
valor_compra = 150.00
cliente_vip = True
primeira_compra = False

# Lógica de desconto
desconto_percentual = 0
if cliente_vip:
    desconto_percentual = 15
elif primeira_compra:
    desconto_percentual = 10
elif valor_compra > 100:
    desconto_percentual = 5

valor_desconto = valor_compra * (desconto_percentual / 100)
valor_final = valor_compra - valor_desconto

print(f"Valor da compra: R$ {valor_compra:.2f}")
print(f"Cliente VIP: {'Sim' if cliente_vip else 'Não'}")
print(f"Desconto aplicado: {desconto_percentual}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final: R$ {valor_final:.2f}")

print("\n🎉 Exemplos práticos concluídos!")