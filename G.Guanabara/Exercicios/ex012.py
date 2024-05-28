preco = float(input('Digite o preço do produto R$ '))
procentagem = 5
d = procentagem * preco / 100
e = preco - d
print('o novo valor do produto com desconto de 5% é R$ {:.2f}'.format(e))