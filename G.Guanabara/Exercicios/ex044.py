'''
    Elabore um programa que calcule o valor a ser pago, por um produto considerando o seu preço normal
    e condição de pagamento:

        A vista dinheiro: 10 % de desconto
        A vista cartao: 5 % de desconto
        Em até 2x no cartao: preço normal
        3x ou mais no cartao: 20 % juros
'''
#Alisson
preco = float(input('\033[1;46mDigite o valor do produto:\033[mR$'))
print(' ')
print(' \033[1;32m[ 1 ] A vista \033[m\n \033[1;33m[ 2 ] Cartao a vista \033[m\n \033[1;34m[ 3 ] até em 2x \033[m\n \033[1;31m[ 4 ] acima de 3x no cartao\033[m')
des1 = 10 * preco / 100
des2 = 5 * preco / 100
juros = 20 * preco/ 100
print(' ')
escolhe = int(input('\033[1;46mEscolha uma opção de pagamento!\033[m '))
print(' ')
print(' ')
if escolhe == 1:
    print('\033[1;32mPreço a vista com 10 % de desconto é R${} com total de R${}\033[m'.format(des1, preco - des1))
elif escolhe == 2:
    print('\033[1;33mPreco a vista no cartao com 5 % de desconto é R${} com total de R${}\033[m'.format(des2, preco - des2))
elif escolhe == 3:
    print('\033[1;34mEm ate 2x no cartao, preço normal é R${}\033[m'.format(preco))
elif escolhe == 4:
    print('\033[1;31m3x ou mais no cartao com 20 % de juros o preco do juros é R${} e o valor total é R${}\033[m'.format(juros, preco + juros))
else:
    print('\033[1;41mOpção invalida, tente novamente!\033[m')