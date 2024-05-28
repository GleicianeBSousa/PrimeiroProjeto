'''
    style: Fonte da letra(negrito, sulinhado e tals)
        0 = none
        1 = bold
        4 = underline
        7 = negative
    
    text: Cor do texo
        30 = branc0
        31 = vermelho
        32 = verde
        33 = amarelo
        34 = azul
        35 = roxo
        36 = zul agua
        37 = cinza

    back: Cor de fundo
        40 = branco
        41 = vermelho
        42 = verde
        43 = amarelo
        44 = azul
        45 = roxo
        46 = azul agua
        47  = cinza
'''
print('\033[1;4;31;43mOlá, mundo\033[m')
print('\033[7mOlá, Mundo!\033[m')
a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a,b))

nome = 'Guanabara'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

nomes = 'Guanabara'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}
print('Ola! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['amarelo'], nome , cores['limpa']))
