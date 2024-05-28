import random
import time

num = random.randint(0, 5)
print(num)
sim = num == int(input('Digite um numero: '))
if sim:
    print('Venceu!')
else:
    print('Perdeu!')

computador = random.randint(0, 5)
print('-=-' * 20)
jogador = int(input('tente adivinhar! '))
print('-=-' * 20)
print('Processando...')
time.sleep(2)
if jogador == computador:
    print('Voce ganhou')
else:
    print('Voce perdeu')