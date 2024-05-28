nome = str(input('Digite seu nome: '))
if nome == 'Gustavo': #condição simples
    print('\033[1;32mQue nome bonito!\033[m')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo': #estrutura aninhada condicional
    print('\033[1;33mSeu nome é bem popular no Brasil!\033[m')
elif nome in 'Ana Claudia Jessica Juliana':
    print('\033[1;35mBelo nome feminino\033[m')
else: #estrututa condicional composta
    print('\033[1;31mSeu nome é bem normal!\033[m')
print('\033[1;34mTenha um bom dia, {}!\033[m'.format(nome))