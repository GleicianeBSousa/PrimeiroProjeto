'''carro = float(input('Digite a velocidade do carro: '))
km = (carro -80) * 7
if carro <=80:
    print('Nao foi multado')
else:
    print('A multa é {:.1f}'.format(km))'''

#condição simples nao usa o else, somente o if
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade >80:
    print('\033[1;30;41m Voce foi multado!\033[m')
    multa = (velocidade-80) * 7
    print('O valor da multa é: \033[1;30;41m{:.2f}\033[m'.format(multa))
print('\033[1;30;42mDigija com segurança!\033[m')