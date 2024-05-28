'''
    Um freelancer esta com dificuldade para calcular qual o valor cobrar por um projeto que esta estimado em 80 horas. Após pensar e revisar o preço de alguns projetos que cobrou no passado, ele montou a seguinte formula:
    valor inicial + qtd de horas estimadas * valor da hora + 15% do valor calculado.
    Crie um programa que faça essa conta para o freelancer. Considere que o valor inicial sempre sera R$1000,00 e o valor da hora cobrada é de R$20,45. A aplicação deve imprimir o valor calculando pelo projeto considerando duas casas decimais na formatação do valor.
    Dica: Preste atenção na ordem que as operações da formula devem ser realizadas.

'''

hora = float(input('Quantas horas você trabalhou? '))
valor_hora = hora*20.45

valor = (valor_hora *15/100) +1000
print(f'A quantidade de hora trabalhada foi {hora} horas e o valor total para receber é R${valor:.2f}')