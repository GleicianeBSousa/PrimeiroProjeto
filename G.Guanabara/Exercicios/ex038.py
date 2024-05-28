''' 
    Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem
     primeiro valor é o maior
     segundo valor é maior
    -nao existe valor maior, os dois sao iguais
'''
#Rodrigo
primeiro_n = int(input("Digite o primeiro Número "))
segundo_n = int(input("Digite o segundo Número "))

if primeiro_n > segundo_n:
    print(f" O {primeiro_n} é Maior que o {segundo_n} ")
elif segundo_n > primeiro_n :
    print(f" O {segundo_n} é Maior que o {primeiro_n} ") 
else:
    print("Não Existe Valor Maoir, Os Dois  Nùmero São Iguais!")


#Alisson
valor1 = int(input('Digite o primeiro valor! '))
valor2 = int(input('Digite o segundo valor! '))

if valor1 > valor2:
    print('\033[1;32mO primeiro é valor maior\033[m')
elif valor2 > valor1:
    print('\033[1;33mO segundo é valor maior\033[m')
else:
    print('\033[1;34mNão existe valor maior os dois sao iguais\033[m')
 