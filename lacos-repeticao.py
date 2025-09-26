# While - o loop se repete enquanto a condição for verdadeira#
# imprimir o numero de 1 a 10 
numero = 1
while (numero <= 25):
    print(numero)
    numero += 1 #incrementa a uma unidade
print('Laço encerrado')

# 
nome = None # inicializa com nada 
while True:
    print('Digite seu nome, ou x para parar')
    nome=input() # se for verdadeiro essa condição ela será encerrada,pelo break.
    if nome == 'x' or nome == 'X': # se o usuario digitar x ou X o laço irá parar
        break  #enqunato for falso, no caso o usuario nao digitar x o loop continuar funcionando
    print(f'Bem-vindo, {nome}')

    