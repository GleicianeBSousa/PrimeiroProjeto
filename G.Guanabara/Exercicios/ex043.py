'''

Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, e acordo com a tabela abaixo:

- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 até 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade mórbida
'''
#Rodrigo

peso_maximo = float(input("Digite Seu peso. "))
altura_maxima = float(input("Digite Sua Altura. "))

imc = (peso_maximo/(altura_maxima**2))

if imc <= 18.5:
    print(f"Seu IMC é\033[1;4;41m{imc:.1f}\033[m você está abaixo do peso.")

elif imc <= 25:
    print(f"Seu IMC é\033[1;4;42m{imc:.1f}\033[mvocê está com peso ideal. ")    

elif imc <= 30:
    print(f"Seu IMC é\033[1;4;43m{imc:.1f}\033[m você está com sobre peso. ") 

elif imc <= 40:
    print(f"Seu IMC é\033[1;4;41m{imc:.1f}\033[m você está com obesidade. ")    
elif imc > 40:
    print(f"Seu IMC é\033[1;4;41m{imc:.1f}\033[m você está com obesidade mórbida. ")     
