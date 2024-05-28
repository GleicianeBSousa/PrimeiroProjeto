'''
    A confederação nacional de natação precisa de um programa que leia o ano de nascimento 
    de um atleta e mostre sua categoria, de acordo com a idade:

        até 9 anos: mirim
        ate 14 anos: infantil
        até 19 anos: junior
        ate 20 anos: senior
        acima: master
'''
#Rodrigo
from datetime import date

data_nascimento = int(input("Digite a sua Data de Nascimento: "))
data_atual = date.today().year
resultado = data_atual - data_nascimento -1

if resultado <= 9:
    print(f"Esse Atleta Têm \033[1;4;45m{resultado} Anos,\033[mEstá Nas Categorias Mirim. ")

elif resultado <= 14:

    print(f"Esse Atleta Têm\033[1;4;45m {resultado} Anos,\033[m Está Nas Categorias Infantil. ")

elif resultado <= 19:
    print(f"Esse Atleta Têm\033[1;4;45m {resultado} Anos,\033[m Está Nas Categorias Junior. ")  

elif resultado <= 20:
    print(f"Esse Atleta Têm\033[1;4;45m {resultado} Anos,\033[m Está Nas Categorias Sênior. ")   

elif resultado > 21:
    print(f"Esse Atleta Têm\033[1;4;45m {resultado} Anos,\033[m Você Já Está Na Categoria Master. ")       
