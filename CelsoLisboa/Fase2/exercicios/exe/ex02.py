'''
    2. Escreva um programa que leia 10 valores inteiros e positivos e  

    a) encontre o maior valor;

    b) encontre o menor valor;

    c) calcule a média dos números lidos.
'''

lista = []
contador = 0
for i in range(1, 11):
    contador += 1
    numeros = int(input("Digite o {}° número. ".format(contador)))
    var = lista.append(numeros)
    if numeros <0:
        print("Digite somente números positivos.") 
        break
maior = max(lista)   
menor = min(lista) 
media = sum(lista) // len(lista)
print("O maior número da lista é {},\nO menor número da lista é {},\nE a média dos números é {}. ".format(maior, menor, media))


