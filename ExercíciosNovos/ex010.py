'''
    Escreva um programa para aprovar o empréstimo bancário
    para a compra de uma casa
    O programa vai perguntar o valor da casa, o salário do comprador e em quantos
    anos ele vai pagar

    Calcule o valor da prestação mensal,
    sabendo que ela não pode exceder 30% do salário
    ou então o empréstimo será negado
'''

casa = float(input('Digite o valor da casa: '))
salario = float(input("Digite o valor do seu salário: "))
tempo = int(input('Digite em quantos anos você deseja pagar a casa: '))
tempo2 = tempo*12
prestacao = casa/tempo2
margem = salario*30/100


if prestacao > margem: #margem = até 30% do salário informado
    print('Empréstimo negado, pois ultrapassa o limite de porcentagem aceito.')

elif prestacao <= margem:
    print(f'O valor da sua prestação fica em {prestacao:.2f} e será pago em {tempo2}')

else:
    print('Opção inválida.')




#print(prestacao)
