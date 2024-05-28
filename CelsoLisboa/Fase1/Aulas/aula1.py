# Calculadora de imc

digite = int(input('Digite o primeiro numero: '))
digite2 = int(input('Digite segundo numero: '))
soma = digite + digite2
print('O primeiro numero é {} e o segundo numero é {} e a soma deles é {}'.format(digite, digite2, soma))

if soma > 10:
    print('É mais que 10')
elif soma < 10:
    print('É menor que 10')
else:
    print('É exatamente 10')