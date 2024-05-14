'''
    Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

'''

produto1 = float(input('Digite o preço do produto: '))
produto2 = float(input('Digite o preço do produto: '))
produto3 = float(input('Digite o preço do produto: '))

if produto1 < produto2 and produto3:
    print(f'Você deve comprar o {produto1} porque é o mais barato.')

elif produto2 < produto1 and produto3:
    print(f'Você deve comprar o {produto2} porque é o mais barato.')

elif produto3 < produto1 and produto2:
    print(f'Você deve comprar o {produto3} porque é o mais barato.')
    