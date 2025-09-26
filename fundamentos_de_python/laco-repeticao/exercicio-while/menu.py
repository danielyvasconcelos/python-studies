#Crie um menu com opções (ex: 1 - Olá, 2 - Sair). 
#O programa só termina quando o usuário escolhe "Sair".


print('====== MENU ======')
print('Opções:')
print('1 - Dizer "Olá Mundo!"')
print('2 - Sair')
entrada = input('Digite um opção:')

while entrada == '1':
    print(' Olá')
    entrada = input('Digite um opção:')
    if entrada == '2':
        print(' Sair')
        break