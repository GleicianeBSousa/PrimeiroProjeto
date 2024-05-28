'''
    Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

import math
angulo = float(input('Leia um valor de um angulo: '))
radiano = math.radians(angulo)
sen = math.sin(radiano)
cos = math.cos(radiano)
tan = math.tan(radiano)
print('O angulo é: {:.2f} o valor de seno é: {:.2f} de cosseno é: {:.2f} e a tangente é: {:.2f}'.format(angulo,sen,cos,tan))

ang = float(input('Qual o valor do angulo: '))
seno = math.sin(math.radians(ang))
cose = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O angulo é: {:.2f} o seno é: {:.2f} o cosseno é: {:.2f} a tangente é: {:.2f}'.format(ang,seno,cose,tang))