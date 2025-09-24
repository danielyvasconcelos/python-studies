# 5. ESCOPO DE VARIÁVEIS

"""
ESCOPO EM PYTHON:
- Variável global: definida fora de funções, acessível em todo o programa
- Variável local: definida dentro de funções, só acessível na função
- Palavra-chave 'global': permite modificar variável global dentro de função
- Palavra-chave 'nonlocal': para variáveis em funções aninhadas
"""

print("=== ESCOPO ===")

# Variável global são as que estão foras da função
variavel_global = "Eu sou global"

def exemplo_escopo():
    # Variável local são as que estão dentro da função
    variavel_local = "Eu sou local"
    print(f"Dentro da função: {variavel_global}")  # Acessa global
    print(f"Dentro da função: {variavel_local}")   # Acessa local
    
    # Modificando variável global
    global variavel_global2
    variavel_global2 = "Global modificada"

exemplo_escopo()
print(f"Fora da função: {variavel_global}")

# Exemplo com nonlocal (funções aninhadas)
def funcao_externa():
    x = "externa"
    
    def funcao_interna():
        nonlocal x
        x = "modificada pela interna"
        print(f"Dentro da interna: {x}")
    
    funcao_interna()
    print(f"Depois da interna: {x}")

print("\n--- Exemplo nonlocal ---")
funcao_externa()

# Regra LEGB (Local, Enclosing, Global, Built-in)
print("\n--- Regra LEGB ---")
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(f"Local: {x}")
    
    inner()
    print(f"Enclosing: {x}")

outer()
print(f"Global: {x}")