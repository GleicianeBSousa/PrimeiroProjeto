num = str(input('Digite um numero até 9999: '))
print('unidade {}'.format(num[3]))
print('dezena {}'.format(num[2]))
print('centena {}'.format(num[1]))
print('milhar {}'.format(num[0]))

mero = int(input('Digite um numero: '))
n = str(mero)
print('unidade {}'.format(n[3]))
print('dezena {}'.format(n[2]))
print('centena {}'.format(n[1]))
print('milhar {}'.format(n[0]))

ero = int(input('Digite um numero: '))
u = ero // 1 % 10
d = ero // 10 % 10
c = ero // 100 % 10
m = ero // 1000 % 10
print('unidade {}'.format(u))
print('dezena {}'.format(d))
print('Centena {}'.format(c))
print('milhar {}'.format(m))


