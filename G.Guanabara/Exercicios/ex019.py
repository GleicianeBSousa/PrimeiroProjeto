import random
alunos = ['alisson', 'caique', 'igor', 'luis']
sorteio = random.choice(alunos)
print('O aluno que vai apagar o quadro é: {}'.format(sorteio))

pr = input('Primeiro aluno: ')
se = input('Segundo aluno: ')
te = input('Terceiro aluno: ')
qu = input('Quarto aluno: ')
sorte = random.choice([pr,se,te,qu])
print('O aluno sorteado foi: {}'.format(sorte))

n1 = input('Aluno 1: ')
n2 = input('Aluno 2: ')
n3 = input('Aluno 3: ')
n4 = input('Aluno 4: ')
lista = [n1,n2,n3,n4]
sor = random.choice(lista)
print('O aluno sorteado é: {}'.format(sor))