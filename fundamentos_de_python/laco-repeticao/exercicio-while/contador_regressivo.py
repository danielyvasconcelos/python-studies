# Contador Regressivo
#Peça ao usuário um número e faça uma contagem regressiva até zero usando while.
#Receita logica 
# Solicite ao usuário que digite um número inteiro inicial para começar a contagem regressiva.
# Verifique se o número digitado é maior ou igual a zero.
# Enquanto o número for maior ou igual a zero:
# Exiba o número atual na tela.
# subtraia 1 do número para continuar a contagem regressiva.

numero = int(input('digite um numero inteiro:'))
while(numero >= 0):
    print(numero)
    numero -= 1