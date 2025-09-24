# OPERADORES DE PERTENCIMENTO EM PYTHON

"""
OPERADORES DE PERTENCIMENTO:
São usados para verificar se um valor está presente em uma sequência ou coleção.
Muito úteis para validações e buscas em estruturas de dados.

LISTA COMPLETA:
in      - Retorna True se o valor está presente na sequência
not in  - Retorna True se o valor NÃO está presente na sequência

FUNCIONAM COM:
- Strings (busca substring ou caractere)
- Listas (busca elemento)
- Tuplas (busca elemento)
- Sets (busca elemento)
- Dicionários (busca chave)
- Ranges (busca número)
"""

print("=== OPERADORES DE PERTENCIMENTO ===")

# OPERADOR IN COM STRINGS
print("=== OPERADOR IN COM STRINGS ===")

frase = "Python é uma linguagem incrível"
print(f"Frase: '{frase}'")

# Busca de caracteres
print(f"\nBusca de caracteres:")
print(f"'P' in frase: {'P' in frase}")
print(f"'z' in frase: {'z' in frase}")
print(f"' ' in frase: {' ' in frase}")  # Espaço

# Busca de substrings
print(f"\nBusca de substrings:")
print(f"'Python' in frase: {'Python' in frase}")
print(f"'Java' in frase: {'Java' in frase}")
print(f"'linguagem' in frase: {'linguagem' in frase}")
print(f"'PYTHON' in frase: {'PYTHON' in frase}")  # Case sensitive

# OPERADOR NOT IN COM STRINGS
print(f"\n=== OPERADOR NOT IN COM STRINGS ===")
print(f"'Java' not in frase: {'Java' not in frase}")
print(f"'Python' not in frase: {'Python' not in frase}")

# OPERADORES COM LISTAS
print(f"\n=== OPERADORES COM LISTAS ===")

numeros = [1, 2, 3, 4, 5]
frutas = ["maçã", "banana", "laranja", "uva"]

print(f"numeros = {numeros}")
print(f"frutas = {frutas}")

print(f"\nBusca em lista de números:")
print(f"3 in numeros: {3 in numeros}")
print(f"6 in numeros: {6 in numeros}")
print(f"0 not in numeros: {0 not in numeros}")

print(f"\nBusca em lista de strings:")
print(f"'banana' in frutas: {'banana' in frutas}")
print(f"'manga' in frutas: {'manga' in frutas}")
print(f"'manga' not in frutas: {'manga' not in frutas}")

# OPERADORES COM TUPLAS
print(f"\n=== OPERADORES COM TUPLAS ===")

coordenadas = (10, 20, 30)
cores = ("azul", "verde", "vermelho")

print(f"coordenadas = {coordenadas}")
print(f"cores = {cores}")

print(f"20 in coordenadas: {20 in coordenadas}")
print(f"'azul' in cores: {'azul' in cores}")
print(f"'amarelo' not in cores: {'amarelo' not in cores}")

# OPERADORES COM SETS
print(f"\n=== OPERADORES COM SETS ===")

conjunto_numeros = {1, 2, 3, 4, 5}
conjunto_letras = {"a", "b", "c", "d"}

print(f"conjunto_numeros = {conjunto_numeros}")
print(f"conjunto_letras = {conjunto_letras}")

print(f"3 in conjunto_numeros: {3 in conjunto_numeros}")
print(f"'c' in conjunto_letras: {'c' in conjunto_letras}")
print(f"'z' not in conjunto_letras: {'z' not in conjunto_letras}")

# OPERADORES COM DICIONÁRIOS
print(f"\n=== OPERADORES COM DICIONÁRIOS ===")
print("Por padrão, busca nas CHAVES do dicionário")

pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print(f"pessoa = {pessoa}")

print(f"\nBusca de chaves:")
print(f"'nome' in pessoa: {'nome' in pessoa}")
print(f"'salario' in pessoa: {'salario' in pessoa}")
print(f"'telefone' not in pessoa: {'telefone' not in pessoa}")

print(f"\nBusca de valores (precisa especificar):")
print(f"'João' in pessoa.values(): {'João' in pessoa.values()}")
print(f"30 in pessoa.values(): {30 in pessoa.values()}")
print(f"'Maria' not in pessoa.values(): {'Maria' not in pessoa.values()}")

print(f"\nBusca de pares chave-valor:")
print(f"('nome', 'João') in pessoa.items(): {('nome', 'João') in pessoa.items()}")
print(f"('idade', 25) in pessoa.items(): {('idade', 25) in pessoa.items()}")

# OPERADORES COM RANGE
print(f"\n=== OPERADORES COM RANGE ===")

intervalo = range(1, 11)  # 1 a 10
print(f"intervalo = range(1, 11)  # {list(intervalo)}")

print(f"5 in intervalo: {5 in intervalo}")
print(f"15 in intervalo: {15 in intervalo}")
print(f"0 not in intervalo: {0 not in intervalo}")

# Range com step
pares = range(0, 21, 2)  # Números pares de 0 a 20
print(f"pares = range(0, 21, 2)  # {list(pares)}")
print(f"10 in pares: {10 in pares}")
print(f"11 in pares: {11 in pares}")

# VALIDAÇÃO DE ENTRADA
print(f"\n=== VALIDAÇÃO DE ENTRADA ===")

def validar_opcao(opcao):
    """Valida se opção está entre as válidas"""
    opcoes_validas = ["sim", "não", "talvez"]
    return opcao.lower() in opcoes_validas

opcoes_teste = ["sim", "SIM", "não", "maybe", "talvez"]
for opcao in opcoes_teste:
    valida = validar_opcao(opcao)
    print(f"Opção '{opcao}': {'Válida' if valida else 'Inválida'}")

# VERIFICAÇÃO DE CARACTERES ESPECIAIS
print(f"\n=== VERIFICAÇÃO DE CARACTERES ESPECIAIS ===")

def tem_caracteres_especiais(senha):
    """Verifica se senha tem caracteres especiais"""
    especiais = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    return any(char in especiais for char in senha)

def validar_senha(senha):
    """Valida senha com múltiplos critérios"""
    if len(senha) < 8:
        return False, "Senha deve ter pelo menos 8 caracteres"
    
    if not any(c.isupper() for c in senha):
        return False, "Senha deve ter pelo menos uma letra maiúscula"
    
    if not any(c.islower() for c in senha):
        return False, "Senha deve ter pelo menos uma letra minúscula"
    
    if not any(c.isdigit() for c in senha):
        return False, "Senha deve ter pelo menos um número"
    
    if not tem_caracteres_especiais(senha):
        return False, "Senha deve ter pelo menos um caractere especial"
    
    return True, "Senha válida"

senhas_teste = [
    "123456",
    "MinhaSenh@123",
    "senhafraca",
    "SENHAFRACA123",
    "SenhaForte@2023"
]

for senha in senhas_teste:
    valida, mensagem = validar_senha(senha)
    print(f"Senha '{senha}': {mensagem}")

# BUSCA EM LISTAS DE DICIONÁRIOS
print(f"\n=== BUSCA EM LISTAS DE DICIONÁRIOS ===")

usuarios = [
    {"nome": "João", "idade": 30, "ativo": True},
    {"nome": "Maria", "idade": 25, "ativo": False},
    {"nome": "Pedro", "idade": 35, "ativo": True},
]

# Buscar usuário por nome
nome_busca = "Maria"
usuario_encontrado = None
for usuario in usuarios:
    if nome_busca in usuario.values():
        usuario_encontrado = usuario
        break

print(f"Busca por '{nome_busca}': {usuario_encontrado}")

# Verificar se existe usuário ativo
tem_usuario_ativo = any(usuario["ativo"] for usuario in usuarios)
print(f"Tem usuário ativo: {tem_usuario_ativo}")

# FILTROS COM PERTENCIMENTO
print(f"\n=== FILTROS COM PERTENCIMENTO ===")

produtos = [
    {"nome": "Notebook", "categoria": "eletrônicos", "tags": ["computador", "portátil"]},
    {"nome": "Mouse", "categoria": "eletrônicos", "tags": ["acessório", "usb"]},
    {"nome": "Livro Python", "categoria": "livros", "tags": ["programação", "python"]},
    {"nome": "Cadeira", "categoria": "móveis", "tags": ["escritório", "conforto"]},
]

# Filtrar produtos por categoria
categorias_interesse = ["eletrônicos", "livros"]
produtos_filtrados = [p for p in produtos if p["categoria"] in categorias_interesse]

print("Produtos de eletrônicos ou livros:")
for produto in produtos_filtrados:
    print(f"  - {produto['nome']}")

# Filtrar produtos por tag
tag_busca = "python"
produtos_com_tag = [p for p in produtos if tag_busca in p["tags"]]

print(f"\nProdutos com tag '{tag_busca}':")
for produto in produtos_com_tag:
    print(f"  - {produto['nome']}")

# VERIFICAÇÃO DE EXTENSÕES DE ARQUIVO
print(f"\n=== VERIFICAÇÃO DE EXTENSÕES DE ARQUIVO ===")

def eh_imagem(nome_arquivo):
    """Verifica se arquivo é uma imagem"""
    extensoes_imagem = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"]
    return any(nome_arquivo.lower().endswith(ext) for ext in extensoes_imagem)

def eh_documento(nome_arquivo):
    """Verifica se arquivo é um documento"""
    extensoes_documento = [".pdf", ".doc", ".docx", ".txt", ".rtf"]
    return any(nome_arquivo.lower().endswith(ext) for ext in extensoes_documento)

arquivos = [
    "foto.jpg",
    "documento.pdf",
    "planilha.xlsx",
    "imagem.PNG",
    "texto.txt",
    "video.mp4"
]

for arquivo in arquivos:
    tipo = []
    if eh_imagem(arquivo):
        tipo.append("imagem")
    if eh_documento(arquivo):
        tipo.append("documento")
    
    tipo_str = ", ".join(tipo) if tipo else "outro"
    print(f"{arquivo:15} - {tipo_str}")

# VERIFICAÇÃO DE PERMISSÕES
print(f"\n=== VERIFICAÇÃO DE PERMISSÕES ===")

def tem_permissao(usuario, acao):
    """Verifica se usuário tem permissão para ação"""
    permissoes_admin = ["criar", "ler", "atualizar", "deletar", "gerenciar"]
    permissoes_editor = ["criar", "ler", "atualizar"]
    permissoes_leitor = ["ler"]
    
    if usuario["tipo"] == "admin":
        return acao in permissoes_admin
    elif usuario["tipo"] == "editor":
        return acao in permissoes_editor
    elif usuario["tipo"] == "leitor":
        return acao in permissoes_leitor
    else:
        return False

usuarios_sistema = [
    {"nome": "Admin", "tipo": "admin"},
    {"nome": "Editor", "tipo": "editor"},
    {"nome": "Leitor", "tipo": "leitor"},
    {"nome": "Visitante", "tipo": "visitante"},
]

acoes = ["ler", "criar", "atualizar", "deletar", "gerenciar"]

print("Matriz de permissões:")
print(f"{'Usuário':10} | {'ler':3} | {'criar':5} | {'atualizar':9} | {'deletar':7} | {'gerenciar':9}")
print("-" * 60)

for usuario in usuarios_sistema:
    linha = f"{usuario['nome']:10} |"
    for acao in acoes:
        pode = "✓" if tem_permissao(usuario, acao) else "✗"
        linha += f" {pode:^{len(acao)+2}} |"
    print(linha)

# BUSCA EM TEXTO
print(f"\n=== BUSCA EM TEXTO ===")

def buscar_palavras_chave(texto, palavras_chave):
    """Busca palavras-chave no texto"""
    texto_lower = texto.lower()
    encontradas = []
    
    for palavra in palavras_chave:
        if palavra.lower() in texto_lower:
            encontradas.append(palavra)
    
    return encontradas

artigo = """
Python é uma linguagem de programação de alto nível, interpretada e de propósito geral.
Foi criada por Guido van Rossum e lançada em 1991. Python é conhecida por sua sintaxe
clara e legível, o que a torna ideal para iniciantes em programação.
"""

palavras_busca = ["Python", "programação", "Guido", "Java", "sintaxe", "1991"]
palavras_encontradas = buscar_palavras_chave(artigo, palavras_busca)

print("Palavras-chave encontradas no artigo:")
for palavra in palavras_encontradas:
    print(f"  - {palavra}")

# PERFORMANCE
print(f"\n=== PERFORMANCE ===")
print("Sets são mais eficientes para verificação de pertencimento")

import time

# Lista grande
lista_grande = list(range(10000))
set_grande = set(lista_grande)

# Busca no final da lista
elemento_busca = 9999

# Teste com lista
start = time.time()
for _ in range(1000):
    resultado = elemento_busca in lista_grande
tempo_lista = time.time() - start

# Teste com set
start = time.time()
for _ in range(1000):
    resultado = elemento_busca in set_grande
tempo_set = time.time() - start

print(f"Tempo busca em lista: {tempo_lista:.6f}s")
print(f"Tempo busca em set: {tempo_set:.6f}s")
print(f"Set é aproximadamente {tempo_lista/tempo_set:.1f}x mais rápido")

# CASOS ESPECIAIS
print(f"\n=== CASOS ESPECIAIS ===")

# Busca em string vazia
print(f"'' in 'Python': {'' in 'Python'}")  # True (substring vazia)
print(f"'a' in '': {'a' in ''}")            # False

# Busca em lista vazia
print(f"1 in []: {1 in []}")                # False
print(f"None in [None]: {None in [None]}")  # True

# Busca com None
lista_com_none = [1, None, 3]
print(f"None in {lista_com_none}: {None in lista_com_none}")  # True

# DICAS E BOAS PRÁTICAS
print(f"\n=== DICAS E BOAS PRÁTICAS ===")
print("1. Use sets para verificações frequentes de pertencimento")
print("2. 'in' com dicionários busca apenas chaves por padrão")
print("3. Para strings, 'in' busca substrings, não apenas caracteres")
print("4. 'not in' é mais legível que 'not (x in y)'")
print("5. Para listas grandes, considere converter para set")

# Exemplo de otimização
def otimizar_busca(lista_valores, valores_busca):
    """Otimiza busca convertendo lista para set"""
    set_valores = set(lista_valores)  # Conversão uma vez
    encontrados = []
    
    for valor in valores_busca:
        if valor in set_valores:  # Busca O(1) em vez de O(n)
            encontrados.append(valor)
    
    return encontrados

lista_test = list(range(1000))
buscar = [100, 500, 999, 1500]
resultado = otimizar_busca(lista_test, buscar)
print(f"\nBusca otimizada encontrou: {resultado}")

print(f"\n✅ Estudo completo sobre operadores de pertencimento!")