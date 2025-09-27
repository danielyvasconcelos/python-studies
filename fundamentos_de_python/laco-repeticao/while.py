# LAÇO DE REPETIÇÃO WHILE EM PYTHON

"""
LAÇO WHILE:
O while é uma estrutura de repetição que executa um bloco de código
ENQUANTO uma condição for verdadeira.

SINTAXE:
while condição:
    # código a ser repetido

CARACTERÍSTICAS:
- Testa a condição ANTES de executar o bloco
- Se a condição for False desde o início, o bloco nunca executa
- Pode criar loops infinitos se a condição nunca se tornar False
- Muito usado quando não sabemos quantas vezes o loop vai executar
"""

print("=== LAÇO DE REPETIÇÃO WHILE ===")

# 1. ESTRUTURA BÁSICA DO WHILE

print("\n=== ESTRUTURA BÁSICA ===")

# Exemplo simples: contar de 1 a 5
contador = 1
print("Contando de 1 a 5:")
while contador <= 5:
    print(f"Número: {contador}")
    contador += 1  # INCREMENTO: adiciona 1 ao contador

print("Loop finalizado!")

# 2. LÓGICA DE INCREMENTO E DECREMENTO

print("\n=== INCREMENTO E DECREMENTO ===")

print("INCREMENTO (+1):")
# Incremento: aumentar o valor da variável
i = 0
while i < 3:
    print(f"i = {i}")
    i += 1  # Equivale a: i = i + 1

print("\nDECREMENTO (-1):")
# Decremento: diminuir o valor da variável
j = 5
while j > 0:
    print(f"j = {j}")
    j -= 1  # Equivale a: j = j - 1

print("\nINCREMENTO DE 2 EM 2:")
# Incremento personalizado
k = 0
while k <= 10:
    print(f"k = {k}")
    k += 2  # Incrementa de 2 em 2

print("\nDECREMENTO DE 3 EM 3:")
# Decremento personalizado
m = 15
while m >= 0:
    print(f"m = {m}")
    m -= 3  # Decrementa de 3 em 3

# 3. DIFERENTES FORMAS DE INCREMENTO/DECREMENTO

print("\n=== FORMAS DE INCREMENTO/DECREMENTO ===")

print("Operadores de atribuição:")
x = 10
print(f"Valor inicial: x = {x}")

x += 5   # x = x + 5
print(f"x += 5: {x}")

x -= 3   # x = x - 3
print(f"x -= 3: {x}")

x *= 2   # x = x * 2
print(f"x *= 2: {x}")

x //= 4  # x = x // 4 (divisão inteira)
print(f"x //= 4: {x}")

# 4. CONDIÇÕES DE PARADA

print("\n=== CONDIÇÕES DE PARADA ===")

print("1. Condição numérica:")
num = 1
while num <= 3:
    print(f"Execução {num}")
    num += 1

print("\n2. Condição booleana:")
continuar = True
tentativas = 0
while continuar:
    tentativas += 1
    print(f"Tentativa {tentativas}")
    if tentativas >= 3:
        continuar = False  # Muda a condição para parar o loop

print("\n3. Condição com string:")
resposta = "sim"
while resposta == "sim":
    print("Executando...")
    resposta = "não"  # Simula mudança de resposta

# 5. LOOP INFINITO E BREAK

print("\n=== LOOP INFINITO E BREAK ===")

print("Usando break para sair do loop:")
contador = 0
while True:  # Loop infinito
    contador += 1
    print(f"Iteração {contador}")
    
    if contador == 3:
        print("Saindo do loop com break!")
        break  # Sai do loop imediatamente

print("Código após o loop")

# 6. CONTINUE - PULAR ITERAÇÃO

print("\n=== CONTINUE - PULAR ITERAÇÃO ===")

print("Pulando números pares:")
numero = 0
while numero < 10:
    numero += 1
    
    if numero % 2 == 0:  # Se for par
        continue  # Pula para a próxima iteração
    
    print(f"Número ímpar: {numero}")

# 7. WHILE COM ELSE

print("\n=== WHILE COM ELSE ===")

print("O else executa quando o while termina normalmente (sem break):")

# Exemplo 1: Termina normalmente
i = 1
while i <= 3:
    print(f"i = {i}")
    i += 1
else:
    print("Loop terminou normalmente - ELSE executado")

print("\nExemplo com break (else NÃO executa):")
j = 1
while j <= 10:
    print(f"j = {j}")
    if j == 2:
        break
    j += 1
else:
    print("Este else NÃO será executado")

# 8. VALIDAÇÃO DE ENTRADA

print("\n=== VALIDAÇÃO DE ENTRADA ===")

print("Simulando validação de entrada:")
# Simulação (normalmente usaria input())
tentativas = 0
senha_correta = "123456"
senhas_teste = ["123", "abc", "123456"]  # Simula entradas do usuário

while tentativas < len(senhas_teste):
    senha = senhas_teste[tentativas]
    print(f"Tentativa {tentativas + 1}: Senha digitada = '{senha}'")
    
    if senha == senha_correta:
        print("Senha correta! Acesso liberado.")
        break
    else:
        print("Senha incorreta. Tente novamente.")
    
    tentativas += 1
else:
    print("Máximo de tentativas excedido!")

# 9. ACUMULADORES

print("\n=== ACUMULADORES ===")

print("1. Soma de números:")
soma = 0
i = 1
while i <= 5:
    soma += i  # Acumula a soma
    print(f"i = {i}, soma acumulada = {soma}")
    i += 1

print(f"Soma final: {soma}")

print("\n2. Produto de números:")
produto = 1
j = 1
while j <= 4:
    produto *= j  # Acumula o produto
    print(f"j = {j}, produto acumulado = {produto}")
    j += 1

print(f"Produto final (fatorial de 4): {produto}")

print("\n3. Contador de ocorrências:")
texto = "python"
letra_busca = "p"
contador_letras = 0
indice = 0

while indice < len(texto):
    if texto[indice] == letra_busca:
        contador_letras += 1
    indice += 1

print(f"A letra '{letra_busca}' aparece {contador_letras} vez(es) em '{texto}'")

# 10. LOOPS ANINHADOS (WHILE DENTRO DE WHILE)

print("\n=== LOOPS ANINHADOS ===")

print("Tabuada do 1 ao 3:")
i = 1
while i <= 3:
    print(f"\nTabuada do {i}:")
    j = 1
    while j <= 5:
        resultado = i * j
        print(f"{i} x {j} = {resultado}")
        j += 1
    i += 1

# 11. EXEMPLOS PRÁTICOS

print("\n=== EXEMPLOS PRÁTICOS ===")

print("1. Contagem regressiva:")
tempo = 5
while tempo > 0:
    print(f"Tempo restante: {tempo}")
    tempo -= 1
print("Tempo esgotado!")

print("\n2. Encontrar o primeiro múltiplo:")
numero = 17
multiplo = numero
while multiplo % 10 != 0:  # Até encontrar múltiplo de 10
    multiplo += numero

print(f"Primeiro múltiplo de {numero} que é múltiplo de 10: {multiplo}")

print("\n3. Sequência de Fibonacci:")
print("Primeiros 8 números da sequência de Fibonacci:")
a, b = 0, 1
contador = 0
while contador < 8:
    print(a, end=" ")
    a, b = b, a + b  # Troca valores e calcula próximo
    contador += 1
print()

print("\n4. Jogo de adivinhação (simulado):")
numero_secreto = 7
palpites = [5, 10, 7]  # Simula palpites do usuário
tentativa = 0

while tentativa < len(palpites):
    palpite = palpites[tentativa]
    print(f"Palpite: {palpite}")
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break
    elif palpite < numero_secreto:
        print("Muito baixo!")
    else:
        print("Muito alto!")
    
    tentativa += 1
else:
    print(f"Fim do jogo! O número era {numero_secreto}")

# 12. CUIDADOS E BOAS PRÁTICAS

print("\n=== CUIDADOS E BOAS PRÁTICAS ===")

print("1. SEMPRE garanta que a condição pode se tornar False:")
print("   ✅ Correto: while i < 10: i += 1")
print("   ❌ Perigoso: while i < 10: pass  # i nunca muda!")

print("\n2. Inicialize variáveis antes do loop:")
print("   ✅ contador = 0")
print("   ✅ while contador < 5:")

print("\n3. Use break para sair de loops infinitos controlados:")
print("   ✅ while True:")
print("       if condicao_saida:")
print("           break")

print("\n4. Cuidado com loops aninhados e break:")
print("   break só sai do loop mais interno")

# Exemplo de loop infinito controlado
print("\n5. Exemplo de menu com loop infinito:")
opcoes_menu = ["1", "2", "0"]  # Simula escolhas do usuário
indice_opcao = 0

while True:
    print("\n--- MENU ---")
    print("1. Opção 1")
    print("2. Opção 2") 
    print("0. Sair")
    
    # Simula entrada do usuário
    if indice_opcao < len(opcoes_menu):
        opcao = opcoes_menu[indice_opcao]
        indice_opcao += 1
    else:
        opcao = "0"
    
    print(f"Opção escolhida: {opcao}")
    
    if opcao == "1":
        print("Executando opção 1...")
    elif opcao == "2":
        print("Executando opção 2...")
    elif opcao == "0":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida!")

# 13. COMPARAÇÃO: WHILE vs FOR

print("\n=== WHILE vs FOR ===")

print("Use WHILE quando:")
print("- Não souber quantas iterações serão necessárias")
print("- A condição de parada depende de algo além de um contador")
print("- Precisar de controle mais flexível sobre o loop")

print("\nUse FOR quando:")
print("- Souber o número exato de iterações")
print("- Iterar sobre uma sequência (lista, string, range)")
print("- Quiser código mais conciso")

print("\nExemplo - mesmo resultado, métodos diferentes:")

print("Com WHILE:")
i = 0
while i < 5:
    print(f"WHILE: {i}")
    i += 1

print("Com FOR:")
for i in range(5):
    print(f"FOR: {i}")

# 14. EXERCÍCIOS PRÁTICOS

print("\n=== EXERCÍCIOS RESOLVIDOS ===")

print("1. Somar números até que a soma seja maior que 50:")
soma = 0
numero = 1
while soma <= 50:
    soma += numero
    numero += 1

print(f"Soma final: {soma}, último número adicionado: {numero-1}")

print("\n2. Contar dígitos de um número:")
numero = 12345
contador_digitos = 0
temp = numero

while temp > 0:
    temp //= 10  # Remove o último dígito
    contador_digitos += 1

print(f"O número {numero} tem {contador_digitos} dígitos")

print("\n3. Inverter um número:")
numero = 12345
numero_invertido = 0
temp = numero

while temp > 0:
    digito = temp % 10  # Pega o último dígito
    numero_invertido = numero_invertido * 10 + digito
    temp //= 10  # Remove o último dígito

print(f"Número original: {numero}")
print(f"Número invertido: {numero_invertido}")

print("\n4. Encontrar o maior divisor comum (MDC):")
a, b = 48, 18
print(f"Calculando MDC de {a} e {b}:")

while b != 0:
    print(f"a = {a}, b = {b}")
    resto = a % b
    a = b
    b = resto

print(f"MDC = {a}")

print("\n✅ Estudo completo sobre laço WHILE finalizado!")
print("\n🎯 RESUMO DOS CONCEITOS:")
print("- while executa ENQUANTO a condição for True")
print("- Sempre garanta que a condição pode se tornar False")
print("- Use incremento (+=) e decremento (-=) para controlar o loop")
print("- break sai do loop, continue pula para próxima iteração")
print("- else executa quando o loop termina normalmente")
print("- Útil para validações, menus, e quando não sabemos quantas iterações")