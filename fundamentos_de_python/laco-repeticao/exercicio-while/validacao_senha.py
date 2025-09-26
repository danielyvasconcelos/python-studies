# Validação de senha

#Peça ao usuário para digitar uma senha até que ele acerte a senha correta (pré-definida).
# Defina uma senha correta previamente no programa.
# Solicite ao usuário que digite uma senha.
# Enquanto a senha digitada for diferente da senha correta:
# Informe ao usuário que a senha está incorreta.
# Solicite novamente que digite a senha.
# Quando o usuário digitar a senha correta, encerre o loop.
# Exiba uma mensagem de sucesso indicando que o acesso foi liberado.

senha_correta = '123456'
senha = input('digite uma senha de 6 digitos numerais: ')
while (senha_correta != senha):
    senha = input('tente novamente:')
    if (senha_correta == senha) :
        print('Parabens, senha correta!')
        break
