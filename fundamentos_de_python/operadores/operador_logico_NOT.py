# OPERADOR LÓGICO NOT EM PYTHON

"""
OPERADOR LÓGICO NOT:
O operador 'not' inverte o valor lógico de uma expressão.
Converte True em False e False em True.

TABELA VERDADE DO NOT:
not True  = False
not False = True

CARACTERÍSTICAS:
- Operador unário (opera sobre um único valor)
- Tem a maior precedência entre os operadores lógicos
- Converte valores truthy em False e falsy em True
- Muito usado para negação de condições
"""

print("=== OPERADOR LÓGICO NOT ===")

# TABELA VERDADE BÁSICA
print("=== TABELA VERDADE ===")
print(f"not True = {not True}")
print(f"not False = {not False}")

# EXEMPLOS COM VARIÁVEIS BOOLEANAS
print(f"\n=== EXEMPLOS COM VARIÁVEIS BOOLEANAS ===")
ativo = True
inativo = False

print(f"ativo = {ativo}")
print(f"not ativo = {not ativo}")
print(f"inativo = {inativo}")
print(f"not inativo = {not inativo}")

# NEGAÇÃO DE COMPARAÇÕES
print(f"\n=== NEGAÇÃO DE COMPARAÇÕES ===")
idade = 16
salario = 2000

print(f"idade = {idade}, salario = {salario}")
print(f"idade >= 18: {idade >= 18}")
print(f"not (idade >= 18): {not (idade >= 18)}")
print(f"salario > 5000: {salario > 5000}")
print(f"not (salario > 5000): {not (salario > 5000)}")

# COMPORTAMENTO COM VALORES TRUTHY/FALSY
print(f"\n=== COMPORTAMENTO COM VALORES TRUTHY/FALSY ===")
print("NOT converte qualquer valor truthy em False e falsy em True")

# Valores falsy em Python
valores_falsy = [False, 0, 0.0, '', [], {}, None]
print(f"\nValores falsy e suas negações:")
for valor in valores_falsy:
    print(f"not {repr(valor):>6} = {not valor}")

# Valores truthy
valores_truthy = [True, 1, -1, 'texto', [1], {'a': 1}, 'False', 42]
print(f"\nValores truthy e suas negações:")
for valor in valores_truthy:
    print(f"not {repr(valor):>8} = {not valor}")

# VERIFICAÇÃO DE EXISTÊNCIA
print(f"\n=== VERIFICAÇÃO DE EXISTÊNCIA ===")

# Verificar se lista está vazia
lista_vazia = []
lista_com_itens = [1, 2, 3]

print(f"Lista vazia: {lista_vazia}")
print(f"not lista_vazia: {not lista_vazia}")  # True (lista vazia é falsy)
print(f"Lista com itens: {lista_com_itens}")
print(f"not lista_com_itens: {not lista_com_itens}")  # False (lista com itens é truthy)

# Verificar se string está vazia
nome = ""
sobrenome = "Silva"

print(f"Nome vazio: '{nome}'")
print(f"not nome: {not nome}")  # True (string vazia é falsy)
print(f"Sobrenome: '{sobrenome}'")
print(f"not sobrenome: {not sobrenome}")  # False (string não vazia é truthy)

# VERIFICAÇÃO DE NONE
print(f"\n=== VERIFICAÇÃO DE NONE ===")
valor = None
outro_valor = 42

print(f"valor = {valor}")
print(f"not valor: {not valor}")  # True (None é falsy)
print(f"outro_valor = {outro_valor}")
print(f"not outro_valor: {not outro_valor}")  # False (42 é truthy)

# Forma mais explícita para verificar None
print(f"valor is None: {valor is None}")
print(f"valor is not None: {valor is not None}")

# PRECEDÊNCIA DO NOT
print(f"\n=== PRECEDÊNCIA DO NOT ===")
print("NOT tem maior precedência que AND e OR")

a = True
b = False
c = True

# NOT é avaliado primeiro
resultado1 = not a and b
resultado2 = (not a) and b  # Equivalente, mais claro
print(f"not a and b = {resultado1}")
print(f"(not a) and b = {resultado2}")

resultado3 = not a or c
resultado4 = (not a) or c  # Equivalente, mais claro
print(f"not a or c = {resultado3}")
print(f"(not a) or c = {resultado4}")

# DUPLA NEGAÇÃO
print(f"\n=== DUPLA NEGAÇÃO ===")
print("Dupla negação converte qualquer valor em booleano")

valores = [0, 1, '', 'texto', [], [1], None, 42]
for valor in valores:
    print(f"not not {repr(valor):>8} = {not not valor}")

# Equivalente a bool()
print(f"\nEquivalente usando bool():")
for valor in valores:
    print(f"bool({repr(valor):>8}) = {bool(valor)}")

# VALIDAÇÃO DE DADOS
print(f"\n=== VALIDAÇÃO DE DADOS ===")

def validar_usuario(nome, email, idade):
    """Valida dados usando NOT para verificar campos obrigatórios"""
    if not nome:
        return False, "Nome é obrigatório"
    
    if not email:
        return False, "Email é obrigatório"
    
    if not idade or idade < 0:
        return False, "Idade deve ser um número positivo"
    
    if not ('@' in email and '.' in email):
        return False, "Email deve ter formato válido"
    
    return True, "Dados válidos"

# Testes de validação
usuarios_teste = [
    ("João", "joao@email.com", 25),
    ("", "email@test.com", 30),      # Nome vazio
    ("Maria", "", 25),               # Email vazio
    ("Pedro", "pedro@test.com", 0),  # Idade zero
    ("Ana", "email_invalido", 28),   # Email sem @
]

for nome, email, idade in usuarios_teste:
    valido, mensagem = validar_usuario(nome, email, idade)
    print(f"Usuário: {nome or 'VAZIO':10} - {mensagem}")

# CONTROLE DE FLUXO
print(f"\n=== CONTROLE DE FLUXO ===")

# Loop while com NOT
contador = 0
numeros = []

print("Adicionando números enquanto lista não tem 5 elementos:")
while not len(numeros) == 5:
    numeros.append(contador)
    contador += 1

print(f"Lista final: {numeros}")

# Verificação de condições de parada
tentativas = 0
max_tentativas = 3
sucesso = False

print(f"\nTentativas de login (máximo {max_tentativas}):")
while not sucesso and tentativas < max_tentativas:
    tentativas += 1
    # Simula tentativa de login
    sucesso = tentativas == 2  # Sucesso na segunda tentativa
    print(f"Tentativa {tentativas}: {'Sucesso' if sucesso else 'Falhou'}")

if not sucesso:
    print("Máximo de tentativas excedido")

# FILTROS E BUSCAS
print(f"\n=== FILTROS E BUSCAS ===")

produtos = [
    {"nome": "Notebook", "ativo": True, "estoque": 10},
    {"nome": "Mouse", "ativo": False, "estoque": 5},
    {"nome": "Teclado", "ativo": True, "estoque": 0},
    {"nome": "Monitor", "ativo": True, "estoque": 3},
]

# Produtos inativos
produtos_inativos = [p for p in produtos if not p["ativo"]]
print("Produtos inativos:")
for produto in produtos_inativos:
    print(f"  - {produto['nome']}")

# Produtos sem estoque
produtos_sem_estoque = [p for p in produtos if not p["estoque"]]
print("Produtos sem estoque:")
for produto in produtos_sem_estoque:
    print(f"  - {produto['nome']}")

# VERIFICAÇÃO DE TIPOS
print(f"\n=== VERIFICAÇÃO DE TIPOS ===")

def processar_valor(valor):
    """Processa valor baseado no tipo"""
    if not isinstance(valor, (int, float)):
        return f"Erro: {valor} não é um número"
    
    if not valor > 0:
        return f"Erro: {valor} deve ser positivo"
    
    return f"Processando: {valor}"

valores_teste = [10, -5, "texto", 0, 3.14, None]
for valor in valores_teste:
    resultado = processar_valor(valor)
    print(resultado)

# VERIFICAÇÃO DE PERMISSÕES
print(f"\n=== VERIFICAÇÃO DE PERMISSÕES ===")

def verificar_acesso(usuario):
    """Verifica se usuário tem acesso negando condições de bloqueio"""
    if not usuario:
        return False, "Usuário não informado"
    
    if not usuario.get("ativo", True):
        return False, "Usuário inativo"
    
    if not usuario.get("email_verificado", False):
        return False, "Email não verificado"
    
    if usuario.get("bloqueado", False):
        return False, "Usuário bloqueado"
    
    return True, "Acesso permitido"

usuarios_teste = [
    {"nome": "João", "ativo": True, "email_verificado": True},
    {"nome": "Maria", "ativo": False, "email_verificado": True},
    {"nome": "Pedro", "ativo": True, "email_verificado": False},
    {"nome": "Ana", "ativo": True, "email_verificado": True, "bloqueado": True},
    None
]

for usuario in usuarios_teste:
    nome = usuario.get("nome", "None") if usuario else "None"
    pode_acessar, motivo = verificar_acesso(usuario)
    print(f"Usuário {nome:5}: {motivo}")

# COMBINANDO NOT COM OUTROS OPERADORES
print(f"\n=== COMBINANDO NOT COM OUTROS OPERADORES ===")

# NOT com AND
x = 10
y = 5
resultado1 = not (x > 15 and y < 3)
print(f"not (x > 15 and y < 3) = {resultado1}")

# NOT com OR (Lei de De Morgan)
resultado2 = not (x > 15 or y > 10)
resultado3 = not x > 15 and not y > 10  # Equivalente pela Lei de De Morgan
print(f"not (x > 15 or y > 10) = {resultado2}")
print(f"not x > 15 and not y > 10 = {resultado3}")

# EXEMPLOS PRÁTICOS
print(f"\n=== EXEMPLOS PRÁTICOS ===")

# Sistema de cache
cache = {}

def obter_dados(chave):
    """Obtém dados do cache ou busca se não existir"""
    if not chave in cache:
        print(f"Buscando dados para '{chave}'...")
        cache[chave] = f"dados_de_{chave}"
    else:
        print(f"Dados encontrados no cache para '{chave}'")
    
    return cache[chave]

print(obter_dados("usuario1"))
print(obter_dados("usuario1"))  # Segunda chamada usa cache

# Validação de formulário
def validar_formulario(dados):
    """Valida formulário verificando campos obrigatórios"""
    erros = []
    
    if not dados.get("nome"):
        erros.append("Nome é obrigatório")
    
    if not dados.get("email"):
        erros.append("Email é obrigatório")
    
    if not dados.get("senha") or len(dados.get("senha", "")) < 6:
        erros.append("Senha deve ter pelo menos 6 caracteres")
    
    return not erros, erros  # Retorna True se não há erros

formularios = [
    {"nome": "João", "email": "joao@test.com", "senha": "123456"},
    {"nome": "", "email": "test@test.com", "senha": "123456"},
    {"nome": "Maria", "email": "", "senha": "123"},
]

for i, form in enumerate(formularios, 1):
    valido, erros = validar_formulario(form)
    print(f"Formulário {i}: {'Válido' if valido else 'Inválido'}")
    if not valido:
        for erro in erros:
            print(f"  - {erro}")

# DICAS E BOAS PRÁTICAS
print(f"\n=== DICAS E BOAS PRÁTICAS ===")
print("1. Use 'not' para inverter condições lógicas")
print("2. 'not valor' é mais pythônico que 'valor == False'")
print("3. Para None, prefira 'is not None' em vez de 'not valor is None'")
print("4. NOT tem maior precedência que AND e OR")
print("5. Use parênteses para clareza: not (a and b)")
print("6. 'not not valor' converte qualquer coisa em bool")

# Comparação de estilos
valor = []
print(f"\nComparação de estilos:")
print(f"Pythônico:    if not valor:")
print(f"Menos claro:  if valor == []:")
print(f"Incorreto:    if valor == False:")

print(f"\n✅ Estudo completo sobre operador lógico NOT!")