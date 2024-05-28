from time import sleep

distancia = float(input('Qual a distancia em km? '))
passagem_curta = 0.50 * distancia
passagem_longa = 0.45 * distancia
print('Calculando...')
sleep(2)
if distancia <=200:
    print('É curta ')
    print('O valor da passagem é: {}'.format(passagem_curta))
else:
    print('É longa ')
    print('O valor da passagem é: {}'.format(passagem_longa))

dis = float(input('Qual distancia em km? '))
print(f'Você vai começar uma viagem {dis}')
if dis <=200:
    preço = dis * 0.50
else:
    preço = dis * 0.45
print('E o preço da sua passagem é {:.2f}'.format(preço))