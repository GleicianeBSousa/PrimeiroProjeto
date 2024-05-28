'''
   Faça um programa que leia um numero e veja qual é o seu sucessor e seu antecessor 
'''
a = int(input('Digite um numero: '))
b = a+1
c = a-1
print('O numero é {} o sucessor é {} e o antecessor é {}'.format(a,b,c))

a = int(input('Digite um numero: '))
print('O valor do numero é {} o sucessor é {} e o antecessor é {}'.format(a, (a+1), (a-1)))