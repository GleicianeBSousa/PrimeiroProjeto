nome = input('Digite uma cidade: ')
if nome.startswith('SANTO'):
    print('Tem')
else:
    print('Nao tem')

cid = str(input('Em que cidade vc nasceu: '))
print(cid[:5] == 'santo')
rem = cid.strip()
n1 = rem[:5] == 'Santo'
print(n1)

dade = str(input('Digite sua cidade: ')).strip()
print(dade[:5].upper() == 'SANTO')
