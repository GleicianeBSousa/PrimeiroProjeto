salario = float(input('Salario é R$ '))
porcentagem = 15
total = porcentagem * salario / 100
aumento = salario + total
print('O novo salario com 15% de aumento é é R$ {:.2f}'.format(aumento))