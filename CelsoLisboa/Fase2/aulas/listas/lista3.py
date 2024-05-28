empresas = ['pao de açucar']
nega_add = str(input('Adicione uma empresa negativada: '))
nega2_add = str(input('Adicione outra empresa negativada: '))
add1 = empresas.append(nega_add)
add2 = empresas.append(nega2_add)
print(f'As empresas {empresas} foram negativadas por falta de pagamento:')
