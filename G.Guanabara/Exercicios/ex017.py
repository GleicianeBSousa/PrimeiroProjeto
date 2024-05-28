'''
     Faça um programa que leia o comprimento do cateto oposto (co) e do cateto adjacente (ca) de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''

from math import sqrt, hypot
b = float(input('Digite o cateto oposto: '))
c = float(input('Digite o cateto adjacente: '))
soma_bc = b**2 + c**2
a = sqrt(soma_bc)
print('O comprimento da hipotenusa é: {:.2f}'.format(a))

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = (co**2 + ca**2)**(1/2)
print('A hipotenusa é: {:.2f}'.format(hi))

cao = float(input('Digite o cateto oposto: '))
caa = float(input('Digite o cateto adjacente: '))
hip = hypot(cao, caa)
print('A hipotenusa é: {:.2f}'.format(hip))
