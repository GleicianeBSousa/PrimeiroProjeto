import math
from time import sleep
num = int(input('\033[1;44mDigite um numero inteiro:\033[m '))
fatorial = math.factorial(num)
print()
print('3')
sleep(1)
print('2')
sleep(1)
print('1')
sleep(1)
print()
print('\033[1;32mO fatorial do numero\033[m \033[1;41m{}\033[m \033[1;32mé\033[m \033[1;41m{}\033[m'.format(num, fatorial))