# Somar números positivos usando while:

#Inicialize uma variável para armazenar a soma dos números positivos.
#Solicite ao usuário que digite um número inteiro.
#Enquanto o número digitado for positivo (maior ou igual a zero):
#Adicione o número à soma.
#Solicite ao usuário que digite outro número inteiro.
#Quando o usuário digitar um número negativo, encerre o loop.
#Exiba o resultado final da soma dos números positivos digitados.

num1 = num2 = None
num1= int(input('Digite o primeiro numero:'))
while (num1 > 0):
    num2= int(input('Digite o primeiro numero:'))
    if num2 < 0 :
        print('loop encerrado')
        break
    else:
        resultado = num1 + num2
        print(f'o resultado da soma dos numeros positivos é {resultado}')