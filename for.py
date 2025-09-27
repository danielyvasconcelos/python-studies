# for item in seguencia 
# instruções executads para cada item da sequência 

lista = [ 2,6,9,4,0,12,3,7]

palavra = 'Dani'
for letra in palavra: # para cada intm dentro da lista façaisso 
    print(letra)

#função auxiliar - range
for numero in range(1,11):# gera do 1 ate o 10 parando no 11 sem gerar ele ou usa (11) como argumento
   print(numero)

for x in range(2,20,2): # valor inicial, valor final, e valor de incremento | valor final, valor inicial e incremento
    print(x)



pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina')
for pedra in pedras: 
    if pedra == 'Quartzo':
        continue # encerra a interação atual do laço, mas nao termina o laço, so nao irá imprimir o quartzo
print(pedra) 


for cont_ex in range(1,6): #bloco principal, ele vai escrever de 1 a 5
    print(f'\nRodada: {cont_ex}')
    for cont_in in range(5, 0, -1):#bloco secundario dentro do bloco princial, ira escrever de tras pra frente decrementando
        print(f'valor: {cont_in}')



import random

for A in range(1,6): # imprime do 1 ao 5
    print(f'\nConjunto {A}')
    for B in range(5):
       numB = random.randint(1,100)
       print(f'Valor: {numB}')

nome =  '#input(digite seu nome)'
for x in range(10):
   print(f'{x+1}  {nome}')