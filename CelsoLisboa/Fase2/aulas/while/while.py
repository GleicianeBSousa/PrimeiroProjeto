var = str(input('Digite sua senha: '))
while var:
    var2 = str(input('Digite sua contra-senha: '))
    if var == var2:
        print('As senhas coincidem!')
        break
    elif var != var2:
        print('Senha incorreta tente novamente!')
        