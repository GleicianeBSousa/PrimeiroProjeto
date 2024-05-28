'''
Uma Nave espacial recebe as pessoas com uma mensagem de boas vindas, de 
acordo com o que elas forneceram ao fazer o cadastro na recepção. 
Crie uma Aplicação que imprima a mensagem de boas vindas, de acordo com
os nomes que estão na lista:  nomes_na_lista = ['Rodrigo','Allison','Victor','Renata'] 
com a seguinte mensagem: 'Olá, O NOME_PESSOA! Seja Bem Vindo  á Nave Imperial Dos Siths!
crie um programa que faça a interpolação da string de boas vinda, substituindo Nome_Pessoa pelo nome 
lido na lista, e imprimindo oa frase de boas vindas, com o nome substituido.
'''

nomes_na_lista = ['Rodrigo','Allison','Victor','Renata'] 

for nome in nomes_na_lista:
    print(f'Olá,{nome} Seja bem vindo á Nave Imperial dos Siths!')


# PODEMOS FAZER DESSE JEITO TAMBÉM:
#print(f'Olá,{nomes_na_lista [0]} Seja bem vindo á Nave Imperial dos Siths!')
#print(f'Olá,{nomes_na_lista [1]} Seja bem vindo á Nave Imperial dos Siths!')
#print(f'Olá,{nomes_na_lista [2]} Seja bem vindo á Nave Imperial dos Siths!')
#print(f'Olá,{nomes_na_lista [3]} Seja bem vindo á Nave Imperial dos Siths!')
