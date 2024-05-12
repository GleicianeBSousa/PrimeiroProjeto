'''
    Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros
'''

metro = float(input('Digite a quantidade de metros: '))
cent = metro/100
milim = metro/1000
print(f'A quantidade de metros é {metro}, em centímetros é {cent} e milímetros é {milim}')
