'''
    Desenvolva um programa que  leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares. se o valor for digitado impar, desconsidere
'''
contador = 0
for i in range(1, 7):
    num = int(input('Digite um numero inteiro: '))
    if num % 2 == 0:
        contador += num
        print('O numero digitado foi \033[2;32m{}\033[m\n e a soma dele é \033[2;31m{}\033[m'.format(num, contador))