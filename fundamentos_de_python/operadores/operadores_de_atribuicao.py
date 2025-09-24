# OPERADORES DE ATRIBUIÇÃO EM PYTHON

"""
OPERADORES DE ATRIBUIÇÃO:
São usados para atribuir valores a variáveis, incluindo operações combinadas.
Permitem modificar o valor de uma variável de forma concisa.

LISTA COMPLETA:
=   (atribuição simples)     - Atribui um valor à variável
+=  (soma e atribui)         - Adiciona e atribui: x += y equivale a x = x + y
-=  (subtrai e atribui)      - Subtrai e atribui: x -= y equivale a x = x - y
*=  (multiplica e atribui)   - Multiplica e atribui: x *= y equivale a x = x * y
/=  (divide e atribui)       - Divide e atribui: x /= y equivale a x = x / y
//= (divisão inteira e atribui) - Divisão inteira e atribui
%=  (módulo e atribui)       - Módulo e atribui: x %= y equivale a x = x % y
**= (potência e atribui)     - Potência e atribui: x **= y equivale a x = x ** y
&=  (AND bit a bit e atribui)
|=  (OR bit a bit e atribui)
^=  (XOR bit a bit e atribui)
>>= (shift direita e atribui)
<<= (shift esquerda e atribui)
"""

print("=== OPERADORES DE ATRIBUIÇÃO ===")

# ATRIBUIÇÃO SIMPLES (=)
print("=== ATRIBUIÇÃO SIMPLES ===")
x = 10
nome = "Python"
lista = [1, 2, 3]
print(f"x = {x}")
print(f"nome = '{nome}'")
print(f"lista = {lista}")

# ATRIBUIÇÃO MÚLTIPLA
print(f"\n=== ATRIBUIÇÃO MÚLTIPLA ===")
a, b, c = 1, 2, 3
print(f"a, b, c = 1, 2, 3 -> a={a}, b={b}, c={c}")

# Atribuição com mesmo valor
x = y = z = 100
print(f"x = y = z = 100 -> x={x}, y={y}, z={z}")

# Troca de valores
a, b = 5, 10
print(f"Antes da troca: a={a}, b={b}")
a, b = b, a
print(f"Após a troca: a={a}, b={b}")

# OPERADORES ARITMÉTICOS DE ATRIBUIÇÃO
print(f"\n=== OPERADORES ARITMÉTICOS DE ATRIBUIÇÃO ===")

# SOMA E ATRIBUI (+=)
numero = 10
print(f"Valor inicial: {numero}")
numero += 5  # numero = numero + 5
print(f"Após += 5: {numero}")

# SUBTRAÇÃO E ATRIBUI (-=)
numero -= 3  # numero = numero - 3
print(f"Após -= 3: {numero}")

# MULTIPLICAÇÃO E ATRIBUI (*=)
numero *= 2  # numero = numero * 2
print(f"Após *= 2: {numero}")

# DIVISÃO E ATRIBUI (/=)
numero /= 4  # numero = numero / 4
print(f"Após /= 4: {numero}")

# DIVISÃO INTEIRA E ATRIBUI (//=)
numero = 17
print(f"\nNovo valor: {numero}")
numero //= 3  # numero = numero // 3
print(f"Após //= 3: {numero}")

# MÓDULO E ATRIBUI (%=)
numero = 17
print(f"Valor: {numero}")
numero %= 5  # numero = numero % 5
print(f"Após %= 5: {numero}")

# POTÊNCIA E ATRIBUI (**=)
numero = 3
print(f"Valor: {numero}")
numero **= 2  # numero = numero ** 2
print(f"Após **= 2: {numero}")

# OPERADORES COM STRINGS
print(f"\n=== OPERADORES COM STRINGS ===")

# Concatenação com +=
texto = "Python"
print(f"Texto inicial: '{texto}'")
texto += " é incrível"  # texto = texto + " é incrível"
print(f"Após += ' é incrível': '{texto}'")

# Repetição com *=
palavra = "Ha"
print(f"Palavra: '{palavra}'")
palavra *= 3  # palavra = palavra * 3
print(f"Após *= 3: '{palavra}'")

# OPERADORES COM LISTAS
print(f"\n=== OPERADORES COM LISTAS ===")

# Adição de elementos com +=
numeros = [1, 2, 3]
print(f"Lista inicial: {numeros}")
numeros += [4, 5]  # numeros = numeros + [4, 5]
print(f"Após += [4, 5]: {numeros}")

# Repetição com *=
lista_pequena = [0]
print(f"Lista: {lista_pequena}")
lista_pequena *= 5  # lista_pequena = lista_pequena * 5
print(f"Após *= 5: {lista_pequena}")

# DIFERENÇA ENTRE += E APPEND
print(f"\n=== DIFERENÇA ENTRE += E APPEND ===")

# Com +=
lista1 = [1, 2, 3]
lista1 += [4, 5]  # Adiciona elementos individuais
print(f"lista1 += [4, 5]: {lista1}")

# Com append
lista2 = [1, 2, 3]
lista2.append([4, 5])  # Adiciona a lista inteira como um elemento
print(f"lista2.append([4, 5]): {lista2}")

# Com extend (similar ao +=)
lista3 = [1, 2, 3]
lista3.extend([4, 5])  # Adiciona elementos individuais
print(f"lista3.extend([4, 5]): {lista3}")

# OPERADORES BIT A BIT DE ATRIBUIÇÃO
print(f"\n=== OPERADORES BIT A BIT DE ATRIBUIÇÃO ===")

# AND bit a bit (&=)
a = 12  # 1100 em binário
print(f"a = {a} (binário: {bin(a)})")
a &= 10  # 1010 em binário, resultado: 1000 (8)
print(f"a &= 10: {a} (binário: {bin(a)})")

# OR bit a bit (|=)
a = 12  # 1100 em binário
print(f"a = {a} (binário: {bin(a)})")
a |= 3   # 0011 em binário, resultado: 1111 (15)
print(f"a |= 3: {a} (binário: {bin(a)})")

# XOR bit a bit (^=)
a = 12  # 1100 em binário
print(f"a = {a} (binário: {bin(a)})")
a ^= 5   # 0101 em binário, resultado: 1001 (9)
print(f"a ^= 5: {a} (binário: {bin(a)})")

# Shift esquerda (<<=)
a = 5   # 101 em binário
print(f"a = {a} (binário: {bin(a)})")
a <<= 2  # Desloca 2 posições à esquerda: 10100 (20)
print(f"a <<= 2: {a} (binário: {bin(a)})")

# Shift direita (>>=)
a = 20  # 10100 em binário
print(f"a = {a} (binário: {bin(a)})")
a >>= 2  # Desloca 2 posições à direita: 101 (5)
print(f"a >>= 2: {a} (binário: {bin(a)})")

# OPERADORES COM SETS
print(f"\n=== OPERADORES COM SETS ===")

# União com |=
conjunto1 = {1, 2, 3}
print(f"Conjunto inicial: {conjunto1}")
conjunto1 |= {3, 4, 5}  # União
print(f"Após |= {{3, 4, 5}}: {conjunto1}")

# Interseção com &=
conjunto2 = {1, 2, 3, 4, 5}
print(f"Conjunto: {conjunto2}")
conjunto2 &= {3, 4, 5, 6}  # Interseção
print(f"Após &= {{3, 4, 5, 6}}: {conjunto2}")

# Diferença simétrica com ^=
conjunto3 = {1, 2, 3}
print(f"Conjunto: {conjunto3}")
conjunto3 ^= {3, 4, 5}  # Diferença simétrica
print(f"Após ^= {{3, 4, 5}}: {conjunto3}")

# CONTADORES E ACUMULADORES
print(f"\n=== CONTADORES E ACUMULADORES ===")

# Contador simples
contador = 0
for i in range(5):
    contador += 1
print(f"Contador final: {contador}")

# Acumulador de soma
soma = 0
numeros = [1, 2, 3, 4, 5]
for num in numeros:
    soma += num
print(f"Soma dos números {numeros}: {soma}")

# Acumulador de produto
produto = 1
for num in [2, 3, 4]:
    produto *= num
print(f"Produto de [2, 3, 4]: {produto}")

# EXEMPLOS PRÁTICOS
print(f"\n=== EXEMPLOS PRÁTICOS ===")

# Sistema de pontuação
pontuacao = 0
print(f"Pontuação inicial: {pontuacao}")

# Acertos e erros
pontuacao += 10  # Acertou uma questão
print(f"Após acerto (+10): {pontuacao}")
pontuacao -= 5   # Errou uma questão
print(f"Após erro (-5): {pontuacao}")
pontuacao *= 2   # Bônus de multiplicador
print(f"Após bônus (x2): {pontuacao}")

# Construção de mensagem
mensagem = "Olá"
mensagem += ", "
mensagem += "mundo"
mensagem += "!"
print(f"Mensagem construída: '{mensagem}'")

# Processamento de lista de compras
carrinho = []
carrinho += ["maçã", "banana"]
carrinho += ["leite"]
print(f"Carrinho: {carrinho}")

# Cálculo de desconto
preco = 100.0
print(f"Preço original: R$ {preco}")
preco *= 0.9  # 10% de desconto
print(f"Preço com desconto: R$ {preco:.2f}")

# PERFORMANCE E CONSIDERAÇÕES
print(f"\n=== PERFORMANCE E CONSIDERAÇÕES ===")

# Para listas, += pode ser mais eficiente que append em loops
import time

# Método com append
lista_append = []
start = time.time()
for i in range(1000):
    lista_append.append(i)
tempo_append = time.time() - start

# Método com +=
lista_plus = []
start = time.time()
for i in range(1000):
    lista_plus += [i]
tempo_plus = time.time() - start

print(f"Tempo com append: {tempo_append:.6f}s")
print(f"Tempo com +=: {tempo_plus:.6f}s")
print("Nota: append é geralmente mais eficiente para adicionar um elemento")

# MUTABILIDADE E IMUTABILIDADE
print(f"\n=== MUTABILIDADE E IMUTABILIDADE ===")

# Com objetos mutáveis (listas)
lista_original = [1, 2, 3]
lista_referencia = lista_original
lista_original += [4, 5]
print(f"Lista original: {lista_original}")
print(f"Lista referência: {lista_referencia}")
print("Ambas foram modificadas (mesmo objeto)")

# Com objetos imutáveis (strings)
string_original = "Python"
string_referencia = string_original
string_original += " é ótimo"
print(f"String original: '{string_original}'")
print(f"String referência: '{string_referencia}'")
print("String referência não mudou (novo objeto criado)")

# VALIDAÇÃO E TRATAMENTO DE ERROS
print(f"\n=== VALIDAÇÃO E TRATAMENTO DE ERROS ===")

# Divisão por zero
numero = 10
try:
    numero /= 0
except ZeroDivisionError:
    print("Erro: Divisão por zero não permitida")

# Operação inválida
try:
    texto = "Python"
    texto += 123  # Erro: não pode concatenar string com int
except TypeError as e:
    print(f"Erro de tipo: {e}")

# DICAS E BOAS PRÁTICAS
print(f"\n=== DICAS E BOAS PRÁTICAS ===")
print("1. Use operadores de atribuição para código mais conciso")
print("2. x += y é mais legível que x = x + y")
print("3. Cuidado com mutabilidade ao usar += com listas")
print("4. Para strings longas, considere usar join() em vez de +=")
print("5. Operadores bit a bit são úteis para flags e máscaras")

# Exemplo de join vs +=
palavras = ["Python", "é", "uma", "linguagem", "incrível"]

# Método menos eficiente
resultado_concat = ""
for palavra in palavras:
    resultado_concat += palavra + " "

# Método mais eficiente
resultado_join = " ".join(palavras)

print(f"Com +=: '{resultado_concat.strip()}'")
print(f"Com join(): '{resultado_join}'")

print(f"\n✅ Estudo completo sobre operadores de atribuição!")