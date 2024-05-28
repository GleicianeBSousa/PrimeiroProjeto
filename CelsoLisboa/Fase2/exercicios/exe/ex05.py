'''
    5   Faça um programa que calcule o valor futuro de uma aplicação
'''
contador = 0
num = float(input('Digite o valor da aplicaçao: '))
tempo = int(input('Digite o tempo da aplicação em anual: '))
taxa = float(input('Digite a taxa de juros anual: '))
contador += 1
taxa_juros = taxa /100
juros = num * (1 + taxa_juros) ** tempo
sotaxa = juros - num
print('O valor inicial da aplicação é R${:.2f}\n o tempo de aplicação em {} anos\n o valor da taxa de juros é {:.2f}%\n o montante dos juros em {} anos é {:.2f} total é {:.2f}'.format(num, tempo, taxa, tempo, sotaxa, juros ))

