'''
    Elabore um programa que calcule o valor a ser pago, por um produto considerando o seu preço normal
    e condição de pagamento:

        A vista dinheiro: 10 % de desconto
        A vista cartao: 5 % de desconto
        Em até 2x no cartao: preço normal
        3x ou mais no cartao: 20 % juros
'''
#Rodrigo
valor_do_produto = float(input("Digite o Valor Do Produto R$ "))
print(" ")
print(" \033[1;4;42m[1] A vista\033[m\n \033[1;4;43m[2] A vista no cartão\033[m\n \033[1;4;44m[3] Parcelado Até 2x sem Juros\033[m\n \033[1;4;41m[4] Parcelado no cartão 3x ou Mais Com Juros\033[m")

a_vista = 10 * valor_do_produto /100
a_vista_no_cartao = 5 * valor_do_produto / 100
parcelado_2x_cartao = valor_do_produto
parcelado_3xoumais_no_cartao = 20 * valor_do_produto  / 100

print(" ")

forma_de_pagamento = int(input("\033[1;4;43mEscolha a Forma De Pagamneto:\033[m " ))

if forma_de_pagamento == 1:

    print(f"\033[1;4;42mVOCÊ PAGOU À VISTA TERÁ UM DESCONTO DE 10%, VAI PAGAR: { valor_do_produto - a_vista :.1F}\033[m ")

elif forma_de_pagamento == 2:
    
    print(f"\033[1;4;43mVOCÊ PAGOU À VISTA TERÁ UM DESCONTO DE 5%, VAI PAGAR: { valor_do_produto - a_vista_no_cartao:.1F}\033[m ")

elif forma_de_pagamento == 3:
    
    print(f" \033[1;4;44mVALOR À PAGAR É: {parcelado_2x_cartao}\033[m ")

elif forma_de_pagamento == 4:
    print(f"\033[1;4;41mVOCÊ TERÁ ACRESCÍMO DE 20%, VAI PAGAR: { valor_do_produto + parcelado_3xoumais_no_cartao:.1F}\033[m ")

else:
    print(" \033[1;4;45mNão Existe Essa Forma de Pagamento\033[m ")

    