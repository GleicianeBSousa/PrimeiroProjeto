'''
     Crie um programa que leia quanto dinheiro em reais uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
'''

real = float(input("Quantos R$ você possui? "))
dolar = float(input("Qual a cotação atual do dolar? "))
#print("Você pode comprar ${:.2f}".format(real/dolar))
print(f"VocÊ pode comprar ${real/dolar:.2f}")
