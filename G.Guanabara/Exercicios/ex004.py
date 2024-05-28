'''
    Faça um programa que leia algo pelo teclado 
    e mostre na tela o seu tipo primitivo 
    e todas as informações possíveis sobre ele
'''

n = input('Digite algo: ')
print(type('O tipo primitivo é {}'.format(n)))
print('Só tem espaços? {}'.format(n.isspace()))
print('É um numero? {}'.format(n.isnumeric()))
print('É alfabetico? {}'.format(n.isalpha()))
print('É alfanumerico? {}'.format(n.isalnum()))
print('Esta em maiusculas? {}'.format(n.isupper()))
print('Esta em minusculas? {}'.format(n.islower()))
print('Esta capitalizada? {}'.format(n.istitle()))