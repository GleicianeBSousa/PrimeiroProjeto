'''
    Aluguel de carros:

    Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado

    Calcule o preço a pagar, sabendo que o carro custa R$ 60 por dia e R$ 0.15 por km rodado
'''

km = float(input('Quantos quilometros foi rodado? '))
dias = int(input('Quantos dias usado? '))
totalkm = km*0.15
totaldias = dias*60
total = (km *0.15) * (dias *60)
print(f'Você pagará pela quilometragem R${totalkm} e total de dias R${totaldias}, com valor final de R${total}') #com f (format) na frente, vc ja vai classificando as variáveis dentro das chaves{}. 
