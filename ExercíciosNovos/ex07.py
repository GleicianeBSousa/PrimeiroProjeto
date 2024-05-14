'''
    Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
'''

import math
angulo = float(input('Digite o ângulo desejado: '))
radi = math.radians(angulo)
seno = math.sin(radi)
cosseno = math.cos(radi)
tangente = math.tan(radi)
print(f'O ângulo é {angulo} e seu seno é {seno:.2f}, seu cosseno é {cosseno:.2f} e sua tangente é {tangente:.2f}')

