'''
    Refaça o exercicio 035 dos triangulos acrescentando o recurso de mostrar 
    que tipo de de triangulo sera formado

        equilatero: todos os lados iguais
        isosceles: dois lados iguais 
        escaleno: todos os lados diferentes
'''
#Rodrigo
triangulo1 = float(input("Digite um Segmento. "))
triangulo2 = float(input("Digite mais um segmento. "))
tringulo3 = float(input("Digite outro segmento. "))

if triangulo1 == triangulo2 == tringulo3:
    print("ESSE É UM TRIÂNGULO EQUILATERO. ")

elif triangulo1 == triangulo2 != tringulo3:
    print("ESSE TRIÂNGULO É ISOSCELES. ")    

elif triangulo1 != triangulo2 != tringulo3:
    print("ESSE TRIÂNGULO É ESCALENO. ")    
