'''
    Faça um programa que leia a largura e a algura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
'''
l = float(input('A largura é: '))
a = float(input('A altura é: '))
c = l * a
d = c / 2
print('A área é {:.2f}m² e a quantidade de tinta necessaria é {:.2f}Lt'.format(c,d))