nome = str(input('Digite seu nome completo: ')).strip()
primeiro = nome.find(" ")
segundo = nome.rfind(" ")
lit_primeiro = nome[:primeiro]
lit_segundo = nome[segundo:]
print(' {}'.format(lit_primeiro))
print('{}'.format(lit_segundo))
n1 = nome.split()
print('O primeiro nome: {}'.format(n1[0]))
print('O ultimo nome: {}'.format(n1[-1]))

nema = str(input('Digite um nome completo: ')).strip()
n = nema.split()
n1 = nema.split()
print('Primeiro nome: {}'.format(n[0]))
print('Segundo nome: {}'.format(n1[-1]))