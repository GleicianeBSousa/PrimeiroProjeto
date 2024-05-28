'''
    Aluguel de carros:

    Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado

    Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado
'''

dias = int(input('Quantos dias alugado? '))
km = float(input('Quantos km rodados? '))
dia_ro = 60
km_ro = 0.15
preco = km * km_ro + dias * dia_ro
print('O total a pagar é R$ {:.2f}'.format(preco))
