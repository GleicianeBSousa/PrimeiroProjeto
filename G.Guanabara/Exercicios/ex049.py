'''
    Faça uma tabuada ultilizando os laços de repetição (ex09)
'''
num = int(input('Digite um valor para calcular a tabuada: '))
for i in range(1, 11):
    print('{} X {:2} = {}'.format(num, i, num * i))