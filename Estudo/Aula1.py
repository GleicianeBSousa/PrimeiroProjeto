'''
Exercicio 1
Crie um aplicativo que calcule o valor total que o sr joão
possue em moedas, A aplicação deve imprimir o valor total r=em reais (R$),
e pode ser utilizado o valor com duas casas decímais no método que for imprimir o valor na tela.
'''

moe35 = 0.05 *35
moe50 = 0.10 *50
moe30 = 0.25 *30
moe15 = 0.50 *15
moe19 = 1.00 *19
total = moe35 + moe50 + moe30 + moe15 + moe19
print('O total de moedas em reais é: R${:.2f}'.format(total))

hora_estimado = 80
valor_inicial = 1000
valor_hora = 20.45
taxa_gordura = 0.15

valor_total = (valor_inicial + hora_estimado * valor_hora ) * (1 + taxa_gordura)

print(f' O valor total de um Freelancer é:{valor_total:.2f}')

###########################################################################################

total_5_centavos = 35 *0.05
total_10_centavos = 50 * 0.10
total_25_centavos = 30 * 0.30
total_50_centavos = 15 * 0.50
total_1_real = 19 * 1.00
total_caixa = (total_5_centavos +total_10_centavos +total_25_centavos + total_50_centavos + total_1_real )