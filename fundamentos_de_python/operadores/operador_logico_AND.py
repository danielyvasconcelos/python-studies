# OPERADOR LÓGICO AND EM PYTHON

"""
OPERADOR LÓGICO AND:
O operador 'and' retorna True apenas quando AMBAS as condições são verdadeiras.
É usado para combinar múltiplas condições que devem ser satisfeitas simultaneamente.

TABELA VERDADE DO AND:
True  and True  = True
True  and False = False
False and True  = False
False and False = False

CARACTERÍSTICAS:
- Avaliação de curto-circuito (short-circuit)
- Se a primeira condição for False, não avalia a segunda
- Retorna o primeiro valor falsy ou o último valor se todos forem truthy
"""

print("=== OPERADOR LÓGICO AND ===")

# TABELA VERDADE BÁSICA
print("=== TABELA VERDADE ===")
print(f"True and True = {True and True}")
print(f"True and False = {True and False}")
print(f"False and True = {False and True}")
print(f"False and False = {False and False}")

# EXEMPLOS COM VARIÁVEIS
print(f"\n=== EXEMPLOS COM VARIÁVEIS ===")
a = True
b = False
c = True

print(f"a = {a}, b = {b}, c = {c}")
print(f"a and b = {a and b}")
print(f"a and c = {a and c}")
print(f"b and c = {b and c}")
print(f"a and b and c = {a and b and c}")

# COMPARAÇÕES COM AND
print(f"\n=== COMPARAÇÕES COM AND ===")
idade = 25
salario = 5000

print(f"idade = {idade}, salario = {salario}")
print(f"idade >= 18 and salario >= 3000: {idade >= 18 and salario >= 3000}")
print(f"idade < 30 and salario > 10000: {idade < 30 and salario > 10000}")

# AVALIAÇÃO DE CURTO-CIRCUITO
print(f"\n=== AVALIAÇÃO DE CURTO-CIRCUITO ===")
print("Se a primeira condição for False, a segunda não é avaliada")

def primeira_condicao():
    print("  Primeira condição avaliada: False")
    return False

def segunda_condicao():
    print("  Segunda condição avaliada: True")
    return True

print("Testando: primeira_condicao() and segunda_condicao()")
resultado = primeira_condicao() and segunda_condicao()
print(f"Resultado: {resultado}")
print("Note que apenas a primeira função foi executada!")

# COMPORTAMENTO COM VALORES TRUTHY/FALSY
print(f"\n=== COMPORTAMENTO COM VALORES TRUTHY/FALSY ===")
print("AND retorna o primeiro valor falsy ou o último valor se todos forem truthy")

# Valores falsy em Python: False, 0, 0.0, '', [], {}, None
valores_falsy = [False, 0, 0.0, '', [], {}, None]
print(f"Valores falsy: {valores_falsy}")

# Valores truthy: qualquer coisa que não seja falsy
valores_truthy = [True, 1, -1, 'texto', [1], {'a': 1}, 'False']
print(f"Valores truthy: {valores_truthy}")

print(f"\nExemplos:")
print(f"5 and 3 = {5 and 3}")  # Retorna 3 (último truthy)
print(f"0 and 5 = {0 and 5}")  # Retorna 0 (primeiro falsy)
print(f"'' and 'Python' = {'' and 'Python'}")  # Retorna '' (primeiro falsy)
print(f"'Hello' and 'World' = {'Hello' and 'World'}")  # Retorna 'World' (último truthy)
print(f"[] and [1, 2] = {[] and [1, 2]}")  # Retorna [] (primeiro falsy)

# MÚLTIPLAS CONDIÇÕES
print(f"\n=== MÚLTIPLAS CONDIÇÕES ===")
nome = "João"
idade = 30
tem_carteira = True
tem_carro = True

print(f"nome = '{nome}', idade = {idade}, tem_carteira = {tem_carteira}, tem_carro = {tem_carro}")

# Verificação para dirigir
pode_dirigir = idade >= 18 and tem_carteira and tem_carro
print(f"Pode dirigir: {pode_dirigir}")

# Verificação para empréstimo
renda = 4000
score = 650
tempo_emprego = 2

pode_emprestimo = renda >= 3000 and score >= 600 and tempo_emprego >= 1
print(f"renda = {renda}, score = {score}, tempo_emprego = {tempo_emprego}")
print(f"Pode fazer empréstimo: {pode_emprestimo}")

# VALIDAÇÃO DE DADOS
print(f"\n=== VALIDAÇÃO DE DADOS ===")

def validar_usuario(nome, email, idade):
    """Valida dados do usuário usando AND"""
    nome_valido = nome and len(nome) >= 2
    email_valido = email and '@' in email and '.' in email
    idade_valida = idade and 18 <= idade <= 120
    
    return nome_valido and email_valido and idade_valida

# Testes de validação
usuarios = [
    ("João Silva", "joao@email.com", 25),
    ("", "email@test.com", 30),  # Nome inválido
    ("Maria", "email_sem_arroba", 25),  # Email inválido
    ("Pedro", "pedro@test.com", 15),  # Idade inválida
    ("Ana", "ana@test.com", 28)  # Todos válidos
]

for nome, email, idade in usuarios:
    valido = validar_usuario(nome, email, idade)
    print(f"Usuário: {nome or 'VAZIO'}, Email: {email}, Idade: {idade} - Válido: {valido}")

# VERIFICAÇÃO DE INTERVALOS
print(f"\n=== VERIFICAÇÃO DE INTERVALOS ===")
numero = 15

# Verificar se está em um intervalo
esta_no_intervalo = numero >= 10 and numero <= 20
print(f"O número {numero} está entre 10 e 20: {esta_no_intervalo}")

# Forma mais pythônica (comparação em cadeia)
esta_no_intervalo_v2 = 10 <= numero <= 20
print(f"Forma pythônica: {esta_no_intervalo_v2}")

# VERIFICAÇÃO DE STRINGS
print(f"\n=== VERIFICAÇÃO DE STRINGS ===")
senha = "MinhaSenh@123"

# Validação de senha complexa
tem_maiuscula = any(c.isupper() for c in senha)
tem_minuscula = any(c.islower() for c in senha)
tem_numero = any(c.isdigit() for c in senha)
tem_especial = any(c in "!@#$%^&*" for c in senha)
tamanho_ok = len(senha) >= 8

senha_forte = tem_maiuscula and tem_minuscula and tem_numero and tem_especial and tamanho_ok

print(f"Senha: '{senha}'")
print(f"Tem maiúscula: {tem_maiuscula}")
print(f"Tem minúscula: {tem_minuscula}")
print(f"Tem número: {tem_numero}")
print(f"Tem caractere especial: {tem_especial}")
print(f"Tamanho >= 8: {tamanho_ok}")
print(f"Senha forte: {senha_forte}")

# COMBINANDO COM OUTROS OPERADORES
print(f"\n=== COMBINANDO COM OUTROS OPERADORES ===")
x = 10
y = 5
z = 15

# AND com OR (precedência: AND tem maior precedência que OR)
resultado1 = x > 5 and y < 10 or z > 20
resultado2 = (x > 5 and y < 10) or z > 20  # Mais claro com parênteses
print(f"x > 5 and y < 10 or z > 20 = {resultado1}")
print(f"(x > 5 and y < 10) or z > 20 = {resultado2}")

# AND com NOT
resultado3 = not (x > 15) and y < 10
print(f"not (x > 15) and y < 10 = {resultado3}")

# EXEMPLOS PRÁTICOS
print(f"\n=== EXEMPLOS PRÁTICOS ===")

# Sistema de acesso
usuario = "admin"
senha_correta = "123456"
horario = 14  # 14h

acesso_permitido = usuario == "admin" and senha_correta == "123456" and 8 <= horario <= 18
print(f"Acesso permitido: {acesso_permitido}")

# Verificação de produto em estoque
produto_existe = True
quantidade_estoque = 10
preco_valido = True

pode_vender = produto_existe and quantidade_estoque > 0 and preco_valido
print(f"Pode vender produto: {pode_vender}")

# Verificação de data
dia = 15
mes = 12
ano = 2023

data_valida = 1 <= dia <= 31 and 1 <= mes <= 12 and ano > 0
print(f"Data {dia}/{mes}/{ano} é válida: {data_valida}")

# DICAS E BOAS PRÁTICAS
print(f"\n=== DICAS E BOAS PRÁTICAS ===")
print("1. Use parênteses para deixar a precedência clara")
print("2. AND tem maior precedência que OR")
print("3. Aproveite o curto-circuito para otimização")
print("4. Para intervalos, use comparação em cadeia: 10 <= x <= 20")
print("5. Cuidado com valores None - use 'is not None' quando necessário")

# Exemplo de verificação com None
valor = None
if valor is not None and valor > 10:
    print("Valor é maior que 10")
else:
    print("Valor é None ou não é maior que 10")

print(f"\n✅ Estudo completo sobre operador lógico AND!")