contador = 0
var = int(input('Digite um numero para tabuada: '))
for temporaria in range(1,11):
    contador += 1
    total = var * contador
    print('{} x {:2} = {}'.format(var, contador, total))