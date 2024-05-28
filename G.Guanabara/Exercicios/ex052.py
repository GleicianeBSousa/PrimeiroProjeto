'''
    Faça um programa que leia um numero inteiro e diga se ele é ou nao um numero primo
'''
num = int(input('Digite um numero inteiro: '))
for i in range(1, num + 1):
    if num / 2:
        print('Não é um numero primo {}'.format(num))
    else:
        print('É um numero primo')


