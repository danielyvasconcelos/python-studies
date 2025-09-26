#5. Tabuada
#Peça um número ao usuário e imprima a tabuada desse número de 1 a 10 usando while.

print('TABUADA')

entrada = int(input('Digite um numero positivo: '))
numero = 0
print(f'Tabuada do {entrada}')
while numero <= 9 :
    numero += 1
    tabuada = numero * entrada
    print(f'{numero} * {entrada} = {tabuada}')

