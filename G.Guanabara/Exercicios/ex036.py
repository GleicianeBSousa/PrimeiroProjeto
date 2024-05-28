valor_casa = float(input('\033[1;33mQual o valor da casa?\033[m '))
salario = float(input('\033[1;33mQual o salario do comprador?\033[m '))
mensalidade = int(input('\033[1;33mQuantas prestações?\033[m '))
prestacao = valor_casa / mensalidade
if prestacao < 30 * salario / 100:
    print('\033[1;32mAprovado!\033[m')
elif prestacao > 30 * salario / 100:
    print('\033[1;31mNão aprovado!\033[m')
