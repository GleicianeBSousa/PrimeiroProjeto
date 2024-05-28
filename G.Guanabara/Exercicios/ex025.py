nome = input('Digite um nome: ').title()
if 'Silva' in nome:
    print('tem')
else:
    print('Nao tem')

real = (nome.find('Silva'))
print(real)
print('Silva' in nome)