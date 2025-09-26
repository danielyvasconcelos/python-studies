media = 0
n1 = n2 = n3 = 0.0
nome, idade = "Fabio", 47

estado = True
# Função print() - imprime na tela
#Função type() -mostra o tipo de dado
print(type(media)) #inteiro
print(type(n1))  #float
print(type(nome))#string
print(type(idade)) #inteiro
print(type(estado)) #bool
print(type(1+2j))# dado complexo

# Função isinstance() - retorna um valor verdadeiro se a variavel for do tipo que voce especificar, se nao for retorna false 
a = 10
b = "sol"
print(isinstance(a, str)) # essa variavel retorna inteiro ? false
print(isinstance(a, int)) # essa variavel retorna inteiro ? false
print(isinstance(a,(int, float))) # essa variavel retorna inteiro ou float ? true

a = 40 
c = 3
resultado = a *c 
print(resultado)
#ctrl + k + c - comenta tudo 
#ctrl + k +u - descomenta tudo

#-----------------------------------------------------------------------------------------------
#repl - read-eval-print loop

#desvios condicional if, if else, if elif else

# if - simples 
numero1 = numero2 = 0.0
media = 0.0
# numero1 =  float(input("digite um numero : "))
# numero2 =  float(input("digite outro numero : "))

#media = (numero1+numero2)/ 2
if (media >= 7):
    print("Aluno aprovado")
#else: 
    #print('aluno reprovado')

#composto
if (media >= 7):
    print("Aluno aprovado")
    print('sua media foi de {}', media)
else: 
    print('aluno reprovado')
    print('sua media foi de', media)



if (media >= 7):
    print("Aluno aprovado")
    print('sua media foi de {}', media)
elif(media >=5 ):
    print('aluno em recuperação')

else: 
    print('aluno reprovado')
    print('sua media foi de {}' .format(media))

#função print()

print('na mesma linha')
print('permanece na mesma linha ', end='')
print('continua na linha')

nome = ' dani'
idade = 25
msg = 'nome dela é {0} e ela tem {1} anos' .format(nome, idade)

print(msg)

#f string , formato de string literal

msg_formatada = f'ola meu nome é {nome}  e eu tenho {idade} anos'

#executar exressões direto na f string
num1 = 10
num2= 5
resposta = f'a soma de {num1} mais {num2} é igual a {num1 + num2}'
print(resposta)

#caracteres de scape
valor = 125.5789
print(f'o valr é \'{valor:.2f}\'')