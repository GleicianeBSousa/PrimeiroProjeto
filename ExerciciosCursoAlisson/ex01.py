'''
   Crie uma aplicação que calcule o valor total que o senhor João possui em moedas real no caixa. Aplicação deve imprimir o valor total em reais e pode utilizar ponto flutuante para representar o valor com duas casas decimais no momento que for imprimir o valor na tela.
   35 moedas de R$0.05
   50 moedas de R$0.10
   30 moedas de R$0.25
   15 moedas de R$0.50
   19 moedas de R$1.00

'''


caixa = 35* 0.05
caixa2 =  50* 0.10
caixa3 = 30* 0.25
caixa4 = 15* 0.50
caixa5 = 19* 1.00
total = caixa + caixa2 + caixa3 + caixa4 + caixa5
#print(f'Temos em moedas de 0.05 o total de {caixa}, moedas de 0.10 o total de {caixa2}')
#print('Temos em moedas de 0.05 o total de {}, moedas de 0.10 o total de {}'.format(caixa, caixa2))
print(f'O total em real é R${total}')
#print('O total em real é R${}'.format(total))