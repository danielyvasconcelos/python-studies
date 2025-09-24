# 10. BOAS PRÁTICAS

"""
BOAS PRÁTICAS PARA VARIÁVEIS EM PYTHON:
- Use nomes descritivos e significativos
- Siga a convenção snake_case para variáveis e funções
- Use MAIÚSCULAS para constantes
- Inicialize variáveis adequadamente
- Evite nomes de uma letra (exceto em loops curtos)
- Não use palavras reservadas
- Seja consistente na nomenclatura
"""

print("=== BOAS PRÁTICAS ===")

# ✅ Use nomes descritivos
idade_usuario = 25
preco_produto = 99.90
print(f"Idade do usuário: {idade_usuario}")
print(f"Preço do produto: R$ {preco_produto}")

# ✅ Use snake_case para variáveis
nome_completo = "João Silva"
data_nascimento = "01/01/1990"
endereco_residencial = "Rua das Flores, 123"

# ✅ Use MAIÚSCULAS para constantes
PI = 3.14159
VELOCIDADE_LUZ = 299792458
TAXA_JUROS = 0.05

# ✅ Inicialize variáveis
contador = 0
lista_vazia = []
dicionario_vazio = {}
total = 0.0

print("Exemplos de boas práticas criados!")

# ❌ EVITE (exemplos do que NÃO fazer):
print("\n=== O QUE EVITAR ===")

# Nomes não descritivos
# x = 25  # Não diz o que representa
# d = "01/01/1990"  # Muito vago

# Nomes muito longos
# nome_completo_do_usuario_cadastrado_no_sistema = "João"

# Misturar convenções
# nomeUsuario = "João"  # camelCase
# nome_usuario = "Maria"  # snake_case
# NomeUsuario = "Pedro"  # PascalCase

# DICAS IMPORTANTES:
print("\n=== DICAS IMPORTANTES ===")

# 1. Use nomes que expressem intenção
is_ativo = True
tem_permissao = False
print(f"Usuário ativo: {is_ativo}")

# 2. Evite abreviações desnecessárias
temperatura_maxima = 35  # Melhor que temp_max
quantidade_produtos = 10  # Melhor que qtd_prod

# 3. Use contexto para nomes mais curtos
class Usuario:
    def __init__(self):
        self.nome = "João"  # Dentro da classe, 'nome' é claro
        self.idade = 25     # Não precisa ser 'idade_usuario'

# 4. Constantes em módulo separado (boa prática)
# config.py
DATABASE_URL = "localhost:5432"
MAX_CONNECTIONS = 100
TIMEOUT_SECONDS = 30

# 5. Use type hints (Python 3.5+)
def calcular_area(largura: float, altura: float) -> float:
    return largura * altura

area = calcular_area(10.0, 5.0)
print(f"Área calculada: {area}")

print("\n✅ Siga essas práticas para código mais legível e maintível!")