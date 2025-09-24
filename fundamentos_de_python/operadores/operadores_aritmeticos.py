# OPERADORES ARITMÉTICOS EM PYTHON

"""
OPERADORES ARITMÉTICOS:
São usados para realizar operações matemáticas básicas e avançadas.
Python suporta todos os operadores matemáticos padrão e alguns especiais.

LISTA COMPLETA:
+ (adição)           - Soma dois valores
- (subtração)        - Subtrai o segundo valor do primeiro
* (multiplicação)    - Multiplica dois valores
/ (divisão)          - Divisão real (retorna float)
// (divisão inteira) - Divisão que retorna apenas a parte inteira
% (módulo)           - Retorna o resto da divisão
** (potenciação)     - Eleva um número à potência de outro
"""

print("=== OPERADORES ARITMÉTICOS ===")

# Valores para demonstração
a = 15
b = 4
print(f"a = {a}, b = {b}")

# ADIÇÃO (+)
soma = a + b
print(f"\nADIÇÃO:")
print(f"{a} + {b} = {soma}")

# SUBTRAÇÃO (-)
subtracao = a - b
print(f"\nSUBTRAÇÃO:")
print(f"{a} - {b} = {subtracao}")

# MULTIPLICAÇÃO (*)
multiplicacao = a * b
print(f"\nMULTIPLICAÇÃO:")
print(f"{a} * {b} = {multiplicacao}")

# DIVISÃO (/)
divisao = a / b
print(f"\nDIVISÃO REAL:")
print(f"{a} / {b} = {divisao}")
print(f"Tipo do resultado: {type(divisao)}")

# DIVISÃO INTEIRA (//)
divisao_inteira = a // b
print(f"\nDIVISÃO INTEIRA:")
print(f"{a} // {b} = {divisao_inteira}")
print(f"Tipo do resultado: {type(divisao_inteira)}")

# MÓDULO (%)
modulo = a % b
print(f"\nMÓDULO (resto da divisão):")
print(f"{a} % {b} = {modulo}")

# POTENCIAÇÃO (**)
potencia = a ** b
print(f"\nPOTENCIAÇÃO:")
print(f"{a} ** {b} = {potencia}")

# PRECEDÊNCIA DOS OPERADORES
print(f"\n=== PRECEDÊNCIA DOS OPERADORES ===")
print("Ordem (maior para menor precedência):")
print("1. ** (potenciação)")
print("2. *, /, //, % (multiplicação, divisões, módulo)")
print("3. +, - (adição, subtração)")

# Exemplos de precedência
resultado1 = 2 + 3 * 4
resultado2 = (2 + 3) * 4
resultado3 = 2 ** 3 * 4
resultado4 = 2 * 3 ** 2

print(f"\nExemplos:")
print(f"2 + 3 * 4 = {resultado1} (multiplicação primeiro)")
print(f"(2 + 3) * 4 = {resultado2} (parênteses primeiro)")
print(f"2 ** 3 * 4 = {resultado3} (potência primeiro)")
print(f"2 * 3 ** 2 = {resultado4} (potência primeiro)")

# OPERADORES COM DIFERENTES TIPOS
print(f"\n=== OPERADORES COM DIFERENTES TIPOS ===")

# Com strings
texto = "Python"
print(f"String * int: '{texto}' * 3 = '{texto * 3}'")
print(f"String + string: 'Hello' + ' World' = '{'Hello' + ' World'}'")

# Com listas
lista = [1, 2, 3]
print(f"Lista * int: {lista} * 2 = {lista * 2}")
print(f"Lista + lista: {lista} + [4, 5] = {lista + [4, 5]}")

# OPERAÇÕES ESPECIAIS
print(f"\n=== OPERAÇÕES ESPECIAIS ===")

# Raiz quadrada usando potenciação
numero = 16
raiz_quadrada = numero ** 0.5
print(f"Raiz quadrada de {numero}: {numero} ** 0.5 = {raiz_quadrada}")

# Potências negativas
print(f"2 ** -3 = {2 ** -3} (equivale a 1/8)")

# Divisão por zero (gera erro)
print(f"\nDivisão por zero:")
try:
    resultado_erro = 10 / 0
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida")

# OPERADORES DE ATRIBUIÇÃO ARITMÉTICA
print(f"\n=== OPERADORES DE ATRIBUIÇÃO ===")
x = 10
print(f"Valor inicial: x = {x}")

x += 5  # x = x + 5
print(f"x += 5: x = {x}")

x -= 3  # x = x - 3
print(f"x -= 3: x = {x}")

x *= 2  # x = x * 2
print(f"x *= 2: x = {x}")

x /= 4  # x = x / 4
print(f"x /= 4: x = {x}")

x //= 2  # x = x // 2
print(f"x //= 2: x = {x}")

x %= 3  # x = x % 3
print(f"x %= 3: x = {x}")

x **= 3  # x = x ** 3
print(f"x **= 3: x = {x}")

# FUNÇÕES MATEMÁTICAS RELACIONADAS
print(f"\n=== FUNÇÕES MATEMÁTICAS BUILT-IN ===")
numeros = [1, -5, 3.14, -2.7, 10]
print(f"Lista: {numeros}")
print(f"abs(-5) = {abs(-5)} (valor absoluto)")
print(f"max({numeros}) = {max(numeros)}")
print(f"min({numeros}) = {min(numeros)}")
print(f"sum({numeros}) = {sum(numeros)}")
print(f"round(3.14159, 2) = {round(3.14159, 2)}")
print(f"pow(2, 3) = {pow(2, 3)} (equivale a 2**3)")

# EXEMPLOS PRÁTICOS
print(f"\n=== EXEMPLOS PRÁTICOS ===")

# Calculadora de IMC
peso = 70
altura = 1.75
imc = peso / (altura ** 2)
print(f"IMC: {peso} / ({altura}²) = {imc:.2f}")

# Conversão de temperatura
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"Temperatura: {celsius}°C = {fahrenheit}°F")

# Cálculo de juros simples
capital = 1000
taxa = 0.05  # 5%
tempo = 2
juros = capital * taxa * tempo
montante = capital + juros
print(f"Juros simples: Capital={capital}, Taxa={taxa*100}%, Tempo={tempo} anos")
print(f"Juros = {juros}, Montante = {montante}")

# Verificar se número é par ou ímpar
numero = 17
eh_par = numero % 2 == 0
print(f"O número {numero} é {'par' if eh_par else 'ímpar'}")

print(f"\n✅ Estudo completo sobre operadores aritméticos!")