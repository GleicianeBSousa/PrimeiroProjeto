'''
    Faça um programa que leia a largura e a algura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m²
'''

altura = float(input("Qual a altura da parede? "))
largura = float(input("Qual a largura da parede? "))
area = altura * largura
#print("Você vai precisar de {} litros de tinta.".format(area/2))
print(f"Você vai precisar de {area/2} litros de tinta.")
print(f'O total da area é {area} e vamos precisar de {area/2} litros.')
