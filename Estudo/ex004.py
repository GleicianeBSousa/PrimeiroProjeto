nomes = input('Digite o nome das pessoas: ').split()
for nome in nomes:
    print('\033[1;32mOlá, \033[1;30;41m{}\033[m \033[1;32mseja bem vindo a nave imperial dos sits\033[m'.format(nome))