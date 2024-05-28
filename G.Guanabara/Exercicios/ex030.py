num = int(input('Digite um numero: '))
if num % 2 == 0:
    print('É par')
elif num % 2 == 1:
    print('É impar')

numero = int(input('Digite um numero: '))
par = numero % 2 == 0
impar = numero % 2 == 1
if par:
    print('É par')
elif impar:
    print('É impar')

n1 = int(input('Digite um numero qualquer: '))
d1 = n1 % 2
if d1 == 0:
    print('É par')
elif d1 == 1:
    print('É impar')