'''
    Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
'''

hora = float(input('Quanto você ganha por hora? '))
hrtrab = float(input('Quantas horas trabalhou no mês: '))
total = hora*hrtrab
print(f'Seu salário pelas suas horas e dias trabalhados é  R${total}')
