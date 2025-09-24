# OPERADOR LÓGICO OR EM PYTHON

"""
OPERADOR LÓGICO OR:
O operador 'or' retorna True quando PELO MENOS UMA das condições é verdadeira.
É usado quando queremos que uma entre várias condições seja satisfeita.

TABELA VERDADE DO OR:
True  or True  = True
True  or False = True
False or True  = True
False or False = False

CARACTERÍSTICAS:
- Avaliação de curto-circuito (short-circuit)
- Se a primeira condição for True, não avalia a segunda
- Retorna o primeiro valor truthy ou o último valor se todos forem falsy
- Tem menor precedência que AND
"""

print("=== OPERADOR LÓGICO OR ===")

# TABELA VERDADE BÁSICA
print("=== TABELA VERDADE ===")
print(f"True or True = {True or True}")
print(f"True or False = {True or False}")
print(f"False or True = {False or True}")
print(f"False or False = {False or False}")

# EXEMPLOS COM VARIÁVEIS
print(f"\n=== EXEMPLOS COM VARIÁVEIS ===")
a = True
b = False
c = True

print(f"a = {a}, b = {b}, c = {c}")
print(f"a or b = {a or b}")
print(f"b or c = {b or c}")
print(f"a or c = {a or c}")
print(f"a or b or c = {a or b or c}")

# COMPARAÇÕES COM OR
print(f"\n=== COMPARAÇÕES COM OR ===")
idade = 16
eh_estudante = True

print(f"idade = {idade}, eh_estudante = {eh_estudante}")
print(f"idade >= 18 or eh_estudante: {idade >= 18 or eh_estudante}")
print(f"idade >= 65 or idade <= 12: {idade >= 65 or idade <= 12}")

# AVALIAÇÃO DE CURTO-CIRCUITO
print(f"\n=== AVALIAÇÃO DE CURTO-CIRCUITO ===")
print("Se a primeira condição for True, a segunda não é avaliada")

def primeira_condicao():
    print("  Primeira condição avaliada: True")
    return True

def segunda_condicao():
    print("  Segunda condição avaliada: False")
    return False

print("Testando: primeira_condicao() or segunda_condicao()")
resultado = primeira_condicao() or segunda_condicao()
print(f"Resultado: {resultado}")
print("Note que apenas a primeira função foi executada!")

# COMPORTAMENTO COM VALORES TRUTHY/FALSY
print(f"\n=== COMPORTAMENTO COM VALORES TRUTHY/FALSY ===")
print("OR retorna o primeiro valor truthy ou o último valor se todos forem falsy")

print(f"\nExemplos:")
print(f"5 or 3 = {5 or 3}")  # Retorna 5 (primeiro truthy)
print(f"0 or 5 = {0 or 5}")  # Retorna 5 (primeiro truthy encontrado)
print(f"'' or 'Python' = {'' or 'Python'}")  # Retorna 'Python' (primeiro truthy)
print(f"'Hello' or 'World' = {'Hello' or 'World'}")  # Retorna 'Hello' (primeiro truthy)
print(f"[] or [1, 2] = {[] or [1, 2]}")  # Retorna [1, 2] (primeiro truthy)
print(f"0 or '' or [] = {0 or '' or []}")  # Retorna [] (último falsy)
print(f"None or False or 0 = {None or False or 0}")  # Retorna 0 (último falsy)

# VALORES PADRÃO COM OR
print(f"\n=== VALORES PADRÃO COM OR ===")
print("Técnica comum para definir valores padrão:")

nome_usuario = ""
nome_padrao = nome_usuario or "Usuário Anônimo"
print(f"Nome: '{nome_usuario}' -> Exibir: '{nome_padrao}'")

configuracao = None
config_padrao = configuracao or {"tema": "claro", "idioma": "pt"}
print(f"Configuração: {configuracao} -> Usar: {config_padrao}")

# Função com parâmetro opcional
def saudar(nome=None):
    nome_final = nome or "Visitante"
    return f"Olá, {nome_final}!"

print(f"saudar(): {saudar()}")
print(f"saudar('João'): {saudar('João')}")
print(f"saudar(''): {saudar('')}")  # String vazia usa padrão

# MÚLTIPLAS CONDIÇÕES
print(f"\n=== MÚLTIPLAS CONDIÇÕES ===")

# Sistema de desconto
idade = 70
eh_estudante = False
eh_funcionario = False

tem_desconto = idade >= 65 or eh_estudante or eh_funcionario
print(f"idade = {idade}, estudante = {eh_estudante}, funcionário = {eh_funcionario}")
print(f"Tem desconto: {tem_desconto}")

# Formas de pagamento aceitas
dinheiro = False
cartao = True
pix = False

pode_pagar = dinheiro or cartao or pix
print(f"dinheiro = {dinheiro}, cartão = {cartao}, pix = {pix}")
print(f"Pode pagar: {pode_pagar}")

# VALIDAÇÃO DE ENTRADA
print(f"\n=== VALIDAÇÃO DE ENTRADA ===")

def validar_entrada(valor):
    """Aceita diferentes tipos de entrada válida"""
    return isinstance(valor, (int, float, str)) and valor not in [None, "", 0]

# Testes
valores_teste = [10, 3.14, "texto", "", 0, None, [], True]
for valor in valores_teste:
    valido = validar_entrada(valor)
    print(f"Valor: {repr(valor):>10} - Válido: {valido}")

# VERIFICAÇÃO DE PERMISSÕES
print(f"\n=== VERIFICAÇÃO DE PERMISSÕES ===")

def tem_acesso(usuario):
    """Verifica se usuário tem acesso baseado em diferentes critérios"""
    eh_admin = usuario.get("tipo") == "admin"
    eh_moderador = usuario.get("tipo") == "moderador"
    tem_permissao_especial = usuario.get("permissao_especial", False)
    
    return eh_admin or eh_moderador or tem_permissao_especial

# Testes de usuários
usuarios = [
    {"nome": "João", "tipo": "admin"},
    {"nome": "Maria", "tipo": "moderador"},
    {"nome": "Pedro", "tipo": "usuario", "permissao_especial": True},
    {"nome": "Ana", "tipo": "usuario"},
]

for usuario in usuarios:
    acesso = tem_acesso(usuario)
    print(f"Usuário {usuario['nome']} ({usuario['tipo']}): Acesso = {acesso}")

# VERIFICAÇÃO DE TIPOS
print(f"\n=== VERIFICAÇÃO DE TIPOS ===")

def eh_numero(valor):
    """Verifica se o valor é um número (int ou float)"""
    return isinstance(valor, int) or isinstance(valor, float)

def eh_sequencia(valor):
    """Verifica se o valor é uma sequência (string, lista ou tupla)"""
    return isinstance(valor, str) or isinstance(valor, list) or isinstance(valor, tuple)

valores = [42, 3.14, "texto", [1, 2, 3], (1, 2), {"a": 1}, True]
for valor in valores:
    print(f"{repr(valor):>15} - É número: {eh_numero(valor):5} - É sequência: {eh_sequencia(valor)}")

# FILTROS E BUSCAS
print(f"\n=== FILTROS E BUSCAS ===")

produtos = [
    {"nome": "Notebook", "categoria": "eletrônicos", "preco": 2500, "promocao": True},
    {"nome": "Mouse", "categoria": "eletrônicos", "preco": 50, "promocao": False},
    {"nome": "Livro Python", "categoria": "livros", "preco": 80, "promocao": True},
    {"nome": "Cadeira", "categoria": "móveis", "preco": 300, "promocao": False},
]

# Produtos em promoção OU baratos (< 100)
produtos_interessantes = []
for produto in produtos:
    if produto["promocao"] or produto["preco"] < 100:
        produtos_interessantes.append(produto["nome"])

print("Produtos em promoção OU baratos:")
for nome in produtos_interessantes:
    print(f"  - {nome}")

# COMBINANDO AND E OR
print(f"\n=== COMBINANDO AND E OR ===")
print("Precedência: AND tem maior precedência que OR")

x = 10
y = 5
z = 15

# Sem parênteses (AND é avaliado primeiro)
resultado1 = x > 5 or y > 10 and z < 20
print(f"x > 5 or y > 10 and z < 20 = {resultado1}")

# Com parênteses para clareza
resultado2 = x > 5 or (y > 10 and z < 20)
print(f"x > 5 or (y > 10 and z < 20) = {resultado2}")

resultado3 = (x > 5 or y > 10) and z < 20
print(f"(x > 5 or y > 10) and z < 20 = {resultado3}")

# VERIFICAÇÃO DE STRINGS VAZIAS
print(f"\n=== VERIFICAÇÃO DE STRINGS VAZIAS ===")

def processar_texto(texto1, texto2, texto3):
    """Processa o primeiro texto não vazio"""
    texto_final = texto1 or texto2 or texto3 or "Texto padrão"
    return f"Processando: '{texto_final}'"

print(processar_texto("", "", "Terceiro texto"))
print(processar_texto("", "Segundo texto", "Terceiro texto"))
print(processar_texto("Primeiro texto", "Segundo texto", "Terceiro texto"))
print(processar_texto("", "", ""))

# VERIFICAÇÃO DE ARQUIVOS/CAMINHOS
print(f"\n=== VERIFICAÇÃO DE ARQUIVOS/CAMINHOS ===")

def encontrar_arquivo_config():
    """Simula busca por arquivo de configuração em diferentes locais"""
    local_usuario = ""  # Simulando que não existe
    local_sistema = "/etc/config.ini"  # Simulando que existe
    local_padrao = "/usr/share/app/default.ini"
    
    arquivo = local_usuario or local_sistema or local_padrao
    return arquivo

config_path = encontrar_arquivo_config()
print(f"Arquivo de configuração encontrado: {config_path}")

# EXEMPLOS PRÁTICOS
print(f"\n=== EXEMPLOS PRÁTICOS ===")

# Sistema de login
def pode_fazer_login(usuario, senha, token_valido=False):
    """Permite login com senha OU token válido"""
    login_senha = usuario == "admin" and senha == "123456"
    login_token = token_valido
    
    return login_senha or login_token

print(f"Login com senha: {pode_fazer_login('admin', '123456')}")
print(f"Login com token: {pode_fazer_login('user', 'wrong', True)}")
print(f"Login inválido: {pode_fazer_login('user', 'wrong', False)}")

# Verificação de horário de funcionamento
def esta_aberto(dia_semana, hora):
    """Verifica se estabelecimento está aberto"""
    # Aberto seg-sex 8-18h OU sáb 9-14h
    dias_uteis = 1 <= dia_semana <= 5 and 8 <= hora <= 18
    sabado = dia_semana == 6 and 9 <= hora <= 14
    
    return dias_uteis or sabado

print(f"Segunda 10h: {esta_aberto(1, 10)}")  # True
print(f"Sábado 12h: {esta_aberto(6, 12)}")   # True
print(f"Domingo 10h: {esta_aberto(7, 10)}")  # False

# DICAS E BOAS PRÁTICAS
print(f"\n=== DICAS E BOAS PRÁTICAS ===")
print("1. Use OR para valores padrão: nome = input_nome or 'Padrão'")
print("2. OR tem menor precedência que AND")
print("3. Use parênteses para deixar a lógica clara")
print("4. Aproveite o curto-circuito para otimização")
print("5. Cuidado com valores falsy inesperados (0, '', [])")

# Exemplo de armadilha com 0
def definir_quantidade(qtd_informada):
    # ERRADO: se qtd_informada for 0, usará o padrão
    # quantidade = qtd_informada or 1
    
    # CORRETO: verificar se é None especificamente
    quantidade = qtd_informada if qtd_informada is not None else 1
    return quantidade

print(f"Quantidade None: {definir_quantidade(None)}")  # 1
print(f"Quantidade 0: {definir_quantidade(0)}")      # 0 (correto)
print(f"Quantidade 5: {definir_quantidade(5)}")      # 5

print(f"\n✅ Estudo completo sobre operador lógico OR!")