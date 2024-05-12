'''
     Faça um programa que leia o comprimento do cateto oposto (co) e do cateto adjacente (ca) de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
'''
# math.atan2(opp, adj)  (???????????)
# hipotenusa = raiz quadrada é a soma dos catetos ao quadrado hipoten=(catop²+catad²)**(1/2)

import math

catop = float(input('Digite o cateto oposto: '))
catad = float(input('Digite o cateto adjacente: '))
#hipotenusa = math.(catop, catad) (???????????)
hipotenusa = (catop **2 + catad **2)**(1/2)
print(hipotenusa)

