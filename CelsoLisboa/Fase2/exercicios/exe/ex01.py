'''
    Faça um programa para calcular o fatorial de um número qualquer
'''
from math import factorial

num = int(input('Digite um numero para o fatorial: '))
fac = factorial(num)
print('O fatorial do numero {} é {}'.format(num, fac))

