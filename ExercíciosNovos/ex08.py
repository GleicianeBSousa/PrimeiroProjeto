'''
    Crie um programa que leia o nome completo de uma pessoa:
        O nome com todas as letras maiúsculas
        O nome com todas minúsculas
        Quantas letras ao todo sem considerar espaços
        Quantas letras tem o primeiro nome:
'''

#variavel = len(variavel) - variavel.count(" ")
#print(textoTam)

nome = str(input('Digite seu nome completo: '))
qtd = len(nome) - nome.count(' ') #forma de saber a qtd de letras dentro de uma string
primeiro_nome = nome.split() #usa .split() para separar um grupo dentro da string
print(nome.upper()) # .upper() é usado para passar tudo para maiúsculo
print(nome.lower()) # .lower() é usado para passar tudo para minúsculo
print(f'Seu nome tem o total de {qtd} letras')
print(f'Seu primeiro nome tem {len(primeiro_nome[0])}')
