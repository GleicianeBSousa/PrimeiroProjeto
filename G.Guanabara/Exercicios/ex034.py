salario = float(input('Qual é o seu salario: '))
por1 = 10
por2 = 15
aumento1 = por1 * salario /100
aumento2 = por2 * salario/100
if salario <=1250:
    print('O aumento foi de {} e o total é {}'.format(aumento2, salario + aumento2))
if salario > 1250:
    print('O aumento foi de {} e o total é {}'.format(aumento1, salario + aumento1))

sal = float(input('Digite seu salario: '))
if sal <= 1250:
    novo = sal + (sal * 15 /100 )
else:
    novo = sal + (sal * 10 /100)
print('Quem ganhava R${} passa a ganhar R${} agora:'.format(salario, novo))