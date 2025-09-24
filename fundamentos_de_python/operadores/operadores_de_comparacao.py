 # OPERADORES DE COMPARAÇÃO EM PYTHON

"""
OPERADORES DE COMPARAÇÃO (RELACIONAIS):
São usados para comparar valores e retornam sempre um valor booleano (True/False).
Essenciais para estruturas condicionais e loops.

LISTA COMPLETA:
== (igual a)           - Verifica se dois valores são iguais
!= (diferente de)      - Verifica se dois valores são diferentes
< (menor que)          - Verifica se o primeiro é menor que o segundo
> (maior que)          - Verifica se o primeiro é maior que o segundo
<= (menor ou igual)    - Verifica se o primeiro é menor ou igual ao segundo
>= (maior ou igual)    - Verifica se o primeiro é maior ou igual ao segundo
is (identidade)        - Verifica se são o mesmo objeto na memória
is not (não identidade)- Verifica se NÃO são o mesmo objeto na memória
"""

print("=== OPERADORES DE COMPARAÇÃO ===")

# Valores para demonstração
a = 10
b = 20
c = 10
print(f"a = {a}, b = {b}, c = {c}")

# IGUALDADE (==)
print(f"\n=== IGUALDADE (==) ===")
print(f"{a} == {b}: {a == b}")
print(f"{a} == {c}: {a == c}")
print(f"'Python' == 'Python': {'Python' == 'Python'}")
print(f"'Python' == 'python': {'Python' == 'python'}")  # Case sensitive

# DIFERENÇA (!=)
print(f"\n=== DIFERENÇA (!=) ===")
print(f"{a} != {b}: {a != b}")
print(f"{a} != {c}: {a != c}")
print(f"'Python' != 'Java': {'Python' != 'Java'}")

# MENOR QUE (<)
print(f"\n=== MENOR QUE (<) ===")
print(f"{a} < {b}: {a < b}")
print(f"{b} < {a}: {b < a}")
print(f"{a} < {c}: {a < c}")

# MAIOR QUE (>)
print(f"\n=== MAIOR QUE (>) ===")
print(f"{a} > {b}: {a > b}")
print(f"{b} > {a}: {b > a}")
print(f"{a} > {c}: {a > c}")

# MENOR OU IGUAL (<=)
print(f"\n=== MENOR OU IGUAL (<=) ===")
print(f"{a} <= {b}: {a <= b}")
print(f"{a} <= {c}: {a <= c}")
print(f"{b} <= {a}: {b <= a}")

# MAIOR OU IGUAL (>=)
print(f"\n=== MAIOR OU IGUAL (>=) ===")
print(f"{a} >= {b}: {a >= b}")
print(f"{a} >= {c}: {a >= c}")
print(f"{b} >= {a}: {b >= a}")

# COMPARAÇÃO COM DIFERENTES TIPOS
print(f"\n=== COMPARAÇÃO COM DIFERENTES TIPOS ===")

# Números (int e float)
print(f"10 == 10.0: {10 == 10.0}")  # True
print(f"10 is 10.0: {10 is 10.0}")  # False (tipos diferentes)

# Strings
print(f"'10' == 10: {'10' == 10}")  # False (tipos diferentes)
print(f"'abc' < 'def': {'abc' < 'def'}")  # Comparação lexicográfica

# Listas
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = [1, 2, 4]
print(f"{lista1} == {lista2}: {lista1 == lista2}")
print(f"{lista1} < {lista3}: {lista1 < lista3}")

# OPERADORES DE IDENTIDADE
print(f"\n=== OPERADORES DE IDENTIDADE (is / is not) ===")

# Diferença entre == e is
x = [1, 2, 3]
y = [1, 2, 3]
z = x

print(f"x = {x}")
print(f"y = {y}")
print(f"z = x (z aponta para o mesmo objeto que x)")

print(f"\nComparando valores (==):")
print(f"x == y: {x == y}")  # True (mesmo conteúdo)
print(f"x == z: {x == z}")  # True (mesmo conteúdo)

print(f"\nComparando identidade (is):")
print(f"x is y: {x is y}")  # False (objetos diferentes)
print(f"x is z: {x is z}")  # True (mesmo objeto)

print(f"\nIDs dos objetos:")
print(f"id(x): {id(x)}")
print(f"id(y): {id(y)}")
print(f"id(z): {id(z)}")

# Casos especiais com is
print(f"\n=== CASOS ESPECIAIS COM 'is' ===")

# Pequenos inteiros são cached pelo Python
a = 256
b = 256
print(f"a = 256, b = 256")
print(f"a is b: {a is b}")  # True (Python cache pequenos inteiros)

a = 257
b = 257
print(f"a = 257, b = 257")
print(f"a is b: {a is b}")  # False (fora do cache)

# None sempre usa is
valor = None
print(f"valor is None: {valor is None}")  # Forma correta
print(f"valor == None: {valor == None}")  # Funciona, mas não recomendado

# COMPARAÇÃO EM CADEIA
print(f"\n=== COMPARAÇÃO EM CADEIA ===")
x = 5
print(f"x = {x}")
print(f"1 < x < 10: {1 < x < 10}")  # Equivale a (1 < x) and (x < 10)
print(f"10 < x < 20: {10 < x < 20}")
print(f"x == 5 == 5: {x == 5 == 5}")

# COMPARAÇÃO DE STRINGS
print(f"\n=== COMPARAÇÃO DE STRINGS ===")
print("Comparação lexicográfica (ordem alfabética):")
print(f"'apple' < 'banana': {'apple' < 'banana'}")
print(f"'Apple' < 'apple': {'Apple' < 'apple'}")  # Maiúsculas vêm antes
print(f"'10' < '2': {'10' < '2'}")  # Comparação de string, não numérica

# Comparação de comprimento vs conteúdo
str1 = "abc"
str2 = "abcd"
print(f"'{str1}' < '{str2}': {str1 < str2}")
print(f"len('{str1}') < len('{str2}'): {len(str1) < len(str2)}")

# COMPARAÇÃO DE COLEÇÕES
print(f"\n=== COMPARAÇÃO DE COLEÇÕES ===")

# Listas
lista_a = [1, 2, 3]
lista_b = [1, 2, 4]
lista_c = [1, 2]
print(f"{lista_a} < {lista_b}: {lista_a < lista_b}")  # Compara elemento por elemento
print(f"{lista_c} < {lista_a}: {lista_c < lista_a}")  # Lista menor é considerada menor

# Tuplas
tupla_a = (1, 2, 3)
tupla_b = (1, 2, 4)
print(f"{tupla_a} < {tupla_b}: {tupla_a < tupla_b}")

# VALORES ESPECIAIS
print(f"\n=== VALORES ESPECIAIS ===")

# Comparação com None
print(f"None == None: {None == None}")
print(f"None is None: {None is None}")
print(f"5 == None: {5 == None}")

# Comparação com booleanos
print(f"True == 1: {True == 1}")
print(f"False == 0: {False == 0}")
print(f"True is 1: {True is 1}")  # False (tipos diferentes)

# EXEMPLOS PRÁTICOS
print(f"\n=== EXEMPLOS PRÁTICOS ===")

# Validação de idade
idade = 25
if 18 <= idade < 65:
    print(f"Idade {idade}: Adulto em idade ativa")

# Validação de nota
nota = 8.5
if nota >= 7:
    status = "Aprovado"
elif nota >= 5:
    status = "Recuperação"
else:
    status = "Reprovado"
print(f"Nota {nota}: {status}")

# Comparação de senhas
senha_digitada = "123456"
senha_correta = "123456"
if senha_digitada == senha_correta:
    print("Login realizado com sucesso!")
else:
    print("Senha incorreta!")

# Verificação de lista vazia
lista = []
if lista == []:  # ou if not lista:
    print("Lista está vazia")

# Verificação de tipo
valor = "Python"
if type(valor) == str:  # Melhor usar isinstance(valor, str)
    print(f"'{valor}' é uma string")

# DICAS IMPORTANTES
print(f"\n=== DICAS IMPORTANTES ===")
print("1. Use 'is' apenas para None, True, False")
print("2. Use '==' para comparar valores")
print("3. Cuidado com comparação de tipos diferentes")
print("4. Strings são comparadas lexicograficamente")
print("5. Listas/tuplas são comparadas elemento por elemento")

print(f"\n✅ Estudo completo sobre operadores de comparação!")