'''
    Crie um algoritmo que leia um número e mostre o seu dobro, o seu triplo e sua raiz quadrada:
'''

# fórmula da raiz quadrada é: **(1/2)
# ou então pode importar da biblioteca math (sqrt)

'''num = float(input('Digite um número: '))
dobro = num*2
triplo = num*3
raiz = num**(1/2)
print(f'O dobro do {num} é {dobro}, seu triplo é {triplo} e sua raiz quadrada é {raiz}')'''

import math
num = float(input('Digite um número: '))
dobro = num*2
triplo = num*3
raiz = math.sqrt(num)
print(f'O dobro do {num} é {dobro}, seu triplo é {triplo} e sua raiz quadrada é {raiz}')