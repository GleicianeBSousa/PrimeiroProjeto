'''
     Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
'''

a = float(input('Carteira: '))
b = 4.94
i = 0.0333659
c = a / b
e = a / i
print('Tem R$ {:.2f} na carteira e pode comprar US$ {:.2f} dolares e comprar ¥ {:.2f} ienes'.format(a,c,e))