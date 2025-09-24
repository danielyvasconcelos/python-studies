# OPERADORES DE IDENTIDADE EM PYTHON

"""
OPERADORES DE IDENTIDADE:
São usados para comparar se duas variáveis referenciam o mesmo objeto na memória.
Diferentes dos operadores de igualdade que comparam valores.

LISTA COMPLETA:
is      - Retorna True se ambas as variáveis apontam para o mesmo objeto
is not  - Retorna True se as variáveis apontam para objetos diferentes

DIFERENÇA FUNDAMENTAL:
== compara VALORES (conteúdo)
is compara IDENTIDADE (mesmo objeto na memória)
"""

print("=== OPERADORES DE IDENTIDADE ===")

# CONCEITO BÁSICO
print("=== CONCEITO BÁSICO ===")
a = [1, 2, 3]
b = [1, 2, 3]  # Mesmo conteúdo, objeto diferente
c = a          # Mesma referência

print(f"a = {a}")
print(f"b = {b}")
print(f"c = a (c aponta para o mesmo objeto que a)")

print(f"\nComparação de valores (==):")
print(f"a == b: {a == b}")  # True (mesmo conteúdo)
print(f"a == c: {a == c}")  # True (mesmo conteúdo)

print(f"\nComparação de identidade (is):")
print(f"a is b: {a is b}")  # False (objetos diferentes)
print(f"a is c: {a is c}")  # True (mesmo objeto)

print(f"\nIDs dos objetos:")
print(f"id(a): {id(a)}")
print(f"id(b): {id(b)}")
print(f"id(c): {id(c)}")

# OPERADOR IS NOT
print(f"\n=== OPERADOR IS NOT ===")
print(f"a is not b: {a is not b}")  # True (objetos diferentes)
print(f"a is not c: {a is not c}")  # False (mesmo objeto)

# CASOS ESPECIAIS - PEQUENOS INTEIROS
print(f"\n=== CASOS ESPECIAIS - PEQUENOS INTEIROS ===")
print("Python mantém cache de inteiros de -5 a 256")

# Inteiros pequenos (cached)
x = 100
y = 100
print(f"x = 100, y = 100")
print(f"x is y: {x is y}")  # True (mesmo objeto no cache)
print(f"id(x): {id(x)}")
print(f"id(y): {id(y)}")

# Inteiros grandes (não cached)
x = 1000
y = 1000
print(f"\nx = 1000, y = 1000")
print(f"x is y: {x is y}")  # False (objetos diferentes)
print(f"id(x): {id(x)}")
print(f"id(y): {id(y)}")

# CASOS ESPECIAIS - STRINGS PEQUENAS
print(f"\n=== CASOS ESPECIAIS - STRINGS PEQUENAS ===")
print("Python pode cachear strings pequenas e simples")

# Strings simples (podem ser cached)
s1 = "python"
s2 = "python"
print(f"s1 = 'python', s2 = 'python'")
print(f"s1 is s2: {s1 is s2}")  # Pode ser True (cached)

# Strings com espaços (menos provável de ser cached)
s3 = "python programming"
s4 = "python programming"
print(f"s3 = 'python programming', s4 = 'python programming'")
print(f"s3 is s4: {s3 is s4}")  # Pode ser False

# VERIFICAÇÃO COM NONE
print(f"\n=== VERIFICAÇÃO COM NONE ===")
print("None é um singleton - sempre use 'is' para comparar com None")

valor1 = None
valor2 = None
valor3 = "None"  # String, não None

print(f"valor1 = None")
print(f"valor2 = None")
print(f"valor3 = 'None' (string)")

print(f"\nComparações corretas:")
print(f"valor1 is None: {valor1 is None}")      # True
print(f"valor2 is None: {valor2 is None}")      # True
print(f"valor3 is None: {valor3 is None}")      # False
print(f"valor1 is valor2: {valor1 is valor2}")  # True (mesmo objeto None)

print(f"\nComparações com == (funcionam, mas não recomendadas):")
print(f"valor1 == None: {valor1 == None}")      # True
print(f"valor3 == None: {valor3 == None}")      # False

# VERIFICAÇÃO COM BOOLEANOS
print(f"\n=== VERIFICAÇÃO COM BOOLEANOS ===")
print("True e False são singletons")

bool1 = True
bool2 = True
bool3 = bool(1)  # Retorna True
bool4 = 1 == 1   # Retorna True

print(f"bool1 = True")
print(f"bool2 = True")
print(f"bool3 = bool(1)")
print(f"bool4 = 1 == 1")

print(f"\nComparações:")
print(f"bool1 is bool2: {bool1 is bool2}")  # True
print(f"bool1 is bool3: {bool1 is bool3}")  # True
print(f"bool1 is bool4: {bool1 is bool4}")  # True
print(f"True is True: {True is True}")      # True

# LISTAS E MUTABILIDADE
print(f"\n=== LISTAS E MUTABILIDADE ===")

# Criando listas
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1
lista4 = lista1.copy()  # Cópia superficial

print(f"lista1 = [1, 2, 3]")
print(f"lista2 = [1, 2, 3]")
print(f"lista3 = lista1")
print(f"lista4 = lista1.copy()")

print(f"\nComparações de identidade:")
print(f"lista1 is lista2: {lista1 is lista2}")  # False
print(f"lista1 is lista3: {lista1 is lista3}")  # True
print(f"lista1 is lista4: {lista1 is lista4}")  # False

# Modificando lista1
lista1.append(4)
print(f"\nApós lista1.append(4):")
print(f"lista1: {lista1}")
print(f"lista2: {lista2}")  # Não mudou
print(f"lista3: {lista3}")  # Mudou (mesma referência)
print(f"lista4: {lista4}")  # Não mudou (cópia)

# DICIONÁRIOS E IDENTIDADE
print(f"\n=== DICIONÁRIOS E IDENTIDADE ===")

dict1 = {"a": 1, "b": 2}
dict2 = {"a": 1, "b": 2}
dict3 = dict1

print(f"dict1 = {dict1}")
print(f"dict2 = {dict2}")
print(f"dict3 = dict1")

print(f"\nComparações:")
print(f"dict1 == dict2: {dict1 == dict2}")  # True (mesmo conteúdo)
print(f"dict1 is dict2: {dict1 is dict2}")  # False (objetos diferentes)
print(f"dict1 is dict3: {dict1 is dict3}")  # True (mesma referência)

# FUNÇÕES E IDENTIDADE
print(f"\n=== FUNÇÕES E IDENTIDADE ===")

def funcao1():
    return "Hello"

def funcao2():
    return "Hello"

funcao3 = funcao1

print(f"funcao1 is funcao2: {funcao1 is funcao2}")  # False
print(f"funcao1 is funcao3: {funcao1 is funcao3}")  # True

# CLASSES E INSTÂNCIAS
print(f"\n=== CLASSES E INSTÂNCIAS ===")

class Pessoa:
    def __init__(self, nome):
        self.nome = nome

pessoa1 = Pessoa("João")
pessoa2 = Pessoa("João")
pessoa3 = pessoa1

print(f"pessoa1.nome: {pessoa1.nome}")
print(f"pessoa2.nome: {pessoa2.nome}")
print(f"pessoa3 = pessoa1")

print(f"\nComparações:")
print(f"pessoa1.nome == pessoa2.nome: {pessoa1.nome == pessoa2.nome}")  # True
print(f"pessoa1 is pessoa2: {pessoa1 is pessoa2}")  # False
print(f"pessoa1 is pessoa3: {pessoa1 is pessoa3}")  # True

# VERIFICAÇÃO DE TIPOS
print(f"\n=== VERIFICAÇÃO DE TIPOS ===")

numero = 42
texto = "42"

print(f"numero = {numero} (tipo: {type(numero)})")
print(f"texto = '{texto}' (tipo: {type(texto)})")

print(f"\nComparações de tipo:")
print(f"type(numero) is int: {type(numero) is int}")
print(f"type(texto) is str: {type(texto) is str}")
print(f"type(numero) is type(texto): {type(numero) is type(texto)}")

# Melhor usar isinstance()
print(f"\nMelhor prática - isinstance():")
print(f"isinstance(numero, int): {isinstance(numero, int)}")
print(f"isinstance(texto, str): {isinstance(texto, str)}")

# OPERADORES EM ESTRUTURAS DE CONTROLE
print(f"\n=== OPERADORES EM ESTRUTURAS DE CONTROLE ===")

def processar_valor(valor):
    """Processa valor baseado em sua identidade"""
    if valor is None:
        return "Valor é None"
    elif valor is True:
        return "Valor é True"
    elif valor is False:
        return "Valor é False"
    else:
        return f"Valor é {valor}"

valores_teste = [None, True, False, 0, 1, "", "texto"]
for valor in valores_teste:
    resultado = processar_valor(valor)
    print(f"{repr(valor):>8}: {resultado}")

# CUIDADOS E ARMADILHAS
print(f"\n=== CUIDADOS E ARMADILHAS ===")

# Armadilha 1: Comparar com is quando deveria usar ==
lista_a = [1, 2, 3]
lista_b = [1, 2, 3]

print("Armadilha 1: Usar 'is' para comparar conteúdo")
print(f"lista_a = {lista_a}")
print(f"lista_b = {lista_b}")
print(f"lista_a == lista_b: {lista_a == lista_b}")  # Correto
print(f"lista_a is lista_b: {lista_a is lista_b}")  # Incorreto para comparar conteúdo

# Armadilha 2: Assumir que objetos iguais são idênticos
x = 1000
y = 1000
print(f"\nArmadilha 2: Assumir identidade para valores grandes")
print(f"x = 1000, y = 1000")
print(f"x == y: {x == y}")  # True
print(f"x is y: {x is y}")  # Pode ser False

# EXEMPLOS PRÁTICOS
print(f"\n=== EXEMPLOS PRÁTICOS ===")

# Cache de objetos
cache = {}

def obter_configuracao(nome):
    """Retorna configuração do cache ou cria nova"""
    if nome not in cache:
        cache[nome] = {"configuracao": f"config_{nome}"}
    return cache[nome]

config1 = obter_configuracao("app")
config2 = obter_configuracao("app")

print(f"config1 is config2: {config1 is config2}")  # True (mesmo objeto do cache)

# Verificação de singleton
class Singleton:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

singleton1 = Singleton()
singleton2 = Singleton()

print(f"singleton1 is singleton2: {singleton1 is singleton2}")  # True

# Verificação de estado padrão
def resetar_lista(lista=None):
    """Reseta lista ou cria nova se None"""
    if lista is None:
        lista = []
    else:
        lista.clear()
    return lista

lista_existente = [1, 2, 3]
lista_nova = resetar_lista()
lista_resetada = resetar_lista(lista_existente)

print(f"Lista nova: {lista_nova}")
print(f"Lista resetada: {lista_resetada}")
print(f"Lista existente após reset: {lista_existente}")

# PERFORMANCE
print(f"\n=== PERFORMANCE ===")
print("'is' é mais rápido que '==' pois compara apenas referências")

import time

# Teste com listas grandes
lista_grande1 = list(range(10000))
lista_grande2 = list(range(10000))
lista_grande3 = lista_grande1

# Teste com ==
start = time.time()
for _ in range(1000):
    resultado = lista_grande1 == lista_grande2
tempo_igual = time.time() - start

# Teste com is
start = time.time()
for _ in range(1000):
    resultado = lista_grande1 is lista_grande3
tempo_is = time.time() - start

print(f"Tempo com ==: {tempo_igual:.6f}s")
print(f"Tempo com is: {tempo_is:.6f}s")
print(f"'is' é aproximadamente {tempo_igual/tempo_is:.1f}x mais rápido")

# DICAS E BOAS PRÁTICAS
print(f"\n=== DICAS E BOAS PRÁTICAS ===")
print("1. Use 'is' apenas para None, True, False")
print("2. Use '==' para comparar valores/conteúdo")
print("3. 'is' é mais rápido que '==' mas tem uso específico")
print("4. Cuidado com cache de inteiros pequenos e strings")
print("5. Para verificar tipo, prefira isinstance() a type() is")
print("6. 'is not' é preferível a 'not ... is'")

# Exemplos de boas práticas
valor = None
if valor is None:  # ✅ Correto
    print("Valor é None")

if valor is not None:  # ✅ Correto
    print("Valor não é None")

# if not valor is None:  # ❌ Menos legível

print(f"\n✅ Estudo completo sobre operadores de identidade!")