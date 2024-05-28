print('Digite suas informações para cadastro!')
email = str(input('Digite seu email: '))
senha = str(input('Digite sua senha: '))
cpf = str(input('Digite seu cpf: '))
nome = str(input('Digite seu nome:'))

dicio = {

    "Email" : email,
    "Senha" : senha,
    "cpf" : cpf,
    "Nome" : nome

}
print(dicio)
conta = str(input("Digite sua contra senha "))
if senha == conta:
    print("senha correta")
elif senha != conta:
    print("Senha incorreta, tente novamente!")