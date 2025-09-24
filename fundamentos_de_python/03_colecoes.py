# 3. TIPOS DE COLEÇÕES

"""
COLEÇÕES EM PYTHON:
- list: mutável, ordenada, permite duplicatas
- tuple: imutável, ordenada, permite duplicatas  
- dict: mutável, chave-valor, chaves únicas
- set: mutável, não ordenado, valores únicos
"""

print("=== COLEÇÕES ===")

# LISTA (list) - Mutável, ordenada, permite duplicatas
frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]
mista = [1, "texto", True, 3.14]
print(f"Lista: {frutas}, tipo: {type(frutas)}")
print(f"Lista: {numeros}, tipo: {type(numeros)}")
print(f"Lista: {mista}, tipo: {type(mista)}")

# TUPLA (tuple) - Imutável, ordenada, permite duplicatas
coordenadas = (10, 20)
cores = ("azul", "verde", "vermelho")
print(f"Tupla: {coordenadas}, tipo: {type(coordenadas)}")
print(f"Tupla: {cores}, tipo: {type(cores)}")

# DICIONÁRIO (dict) - Mutável, chave-valor, não permite chaves duplicadas
pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
print(f"Dicionário: {pessoa}, tipo: {type(pessoa)}")

# CONJUNTO (set) - Mutável, não ordenado, não permite duplicatas
numeros_unicos = {1, 2, 3, 4, 5}
letras = {"a", "b", "c"}
print(f"Set: {numeros_unicos}, tipo: {type(numeros_unicos)}")

# Exemplos de operações básicas
print(f"\nOperações básicas:")
print(f"Tamanho da lista: {len(frutas)}")
print(f"Primeiro item da tupla: {coordenadas[0]}")
print(f"Valor do dicionário: {pessoa['nome']}")
print(f"União de sets: {numeros_unicos | {6, 7, 8}}")