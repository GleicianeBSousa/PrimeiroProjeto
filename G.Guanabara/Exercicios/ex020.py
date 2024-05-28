import random

alunos = ['Alisson','Igor','Caique','Luis']
sorteio = list(enumerate(alunos))
for i in range(len(alunos)):
    print('A ordem vai ser: {}'.format(sorteio))

n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem de apresentação sera: {}'.format(lista))