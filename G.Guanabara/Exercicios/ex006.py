'''
    Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada:
'''

a = int(input('Digite um numero: '))
b = a*2
c = a*3
d = a**(1/2)
print('O numero é {} \n o dobro é {} \n o triplo é {} \n e a raiz quadrada é {:.2f} \n'.format(a,b,c,d))