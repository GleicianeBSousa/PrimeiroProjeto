'''
    Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
    No final, mostre os 10 primeiros termos da progressao
    Formula: am = a2 + (n-1)*R
    REFAZER ELE DEPOIS
'''

termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo = termo + (10 - 1) * razao
for i in range(termo, decimo + razao, razao):
    print('{} → '.format(i), end='')
print('ACABOU')