horas_trabalhadas = 80
valor_hora = 20.45
valor_inicial = 1000
total = horas_trabalhadas * valor_hora + valor_inicial
taxa_gordura = 15 *total /100
print('\033[1;32mO valor do trabalho é \033[1;30;41mR${:.2f}\033[m \033[1;32me a porcetegaem é \033[1;30;41mR${:.2f}\033[m \033[1;32me o total com a porcentagem é: \033[1;30;41mR${:.2f}\033[m'.format(total, taxa_gordura, total+taxa_gordura))
