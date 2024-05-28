'''
FuI EM UMA LOJA COMPRA UM VESTIDO PRA MINHA ESPOSA, O VENDEDOR NA HORA Do PAGAMENTO, 
DISSE  QUE O VESTIDO ESTAVA COM 20% DE DESCONTO NO PAGAMENTO EM DINHEIRO.
SABENDO QUE O VESTIDO CUSTA R$ 200 REAIS, QUAL O VALOR DO VESTIDO COM DESCONTO.

AQUI EU CRIEI UM PROGRAMA QUE A VENDEDORA, COLOCA O VALOR DO VESTIDO E O DESCONTO A SER DADO.
'''
custo_do_vestido = float(input('Digite o Valor do Vestido:'))
valor_do_desconto = float(input('Digite o Valor do Desconto:'))


valor_com_desconto = custo_do_vestido * (1 - valor_do_desconto)
print(f' O valor do vestido com desconto é R${valor_com_desconto:.2f}')

# PODEMOS USAR ESSE DE CIMA, OU ESSE AQUI: valor_com_desconto = round(valor_com_desconto,2)
'''
 dica: podemos usar nas vareáveis como boa prática, o uso de snak_case ou camel_case
 O snake_case, é quando não utilizamos letras maiúsculas no inicio de cada letra ex: nome_aluno =
 O uso do camel_case, é quando colocamos a primeira letra da variável em maiúsculo ex: Nome_Aluno =
'''

