'''
    Crie um programa que faça o computador jogar pedra, papel e tesoura com vc
'''
from random import choice
print('\033[1;46mEscolha uma opção!\033[m')
print(' ')
print('\033[1;42m[ Pedra ]\033[m\n\033[1;43m[ Papel ]\033[m\n\033[1;44m[ Tesoura ]\033[m')
print(' ')
lista = ['Pedra', 'Papel', 'Tesoura']
jogador = (input('\033[1;47m Digite uma opção \033[m')).capitalize()
maquina = choice(lista)
print(' ')
print('\033[1;36mA maquina escolheu\033[m \033[1;46m{}\033[m'.format(maquina))
if jogador == maquina:
    print('\033[1;32mEmpate\033[m')
elif jogador == 'Pedra' and maquina == 'Tesoura':
    print('\033[1;33mVoce ganhou\033[m')
elif jogador == 'Papel' and maquina == 'Pedra':
    print('\033[1;34mVoce ganhou\033[m')
elif jogador == 'Tesoura' and maquina == 'Papel':
    print('\033[1;35mVoce ganhou\033[m')
elif maquina == 'Pedra' and jogador == 'Tesoura':
    print('\033[1;33mA maquina ganhou!\033[m')
elif maquina == 'Papel' and jogador == 'Pedra':
    print('\033[1;34mA maquina ganhou!\033[m')
elif maquina == 'Tesoura' and jogador == 'Papel':
    print('\033[1;35mA maquina ganhou\033[m')
else:
    print('\033[1;41mOpção invalida\033[m')
#fala ae rodrigo