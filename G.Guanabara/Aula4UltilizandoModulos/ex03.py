from math import sqrt, floor
num = int(input('Digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual há {:.2f}'.format(num, floor(raiz)))