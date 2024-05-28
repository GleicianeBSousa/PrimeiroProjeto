#cada um desses segmentos tem que ser menor do que a soma do comprimento dos outros dois
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
'''if r1 + r2 < r3:
    print('Forma um triangulo1 ')
elif r2 + r3 < r1:
    print('Forma um triangulo2')
elif r3 + r1 < r2:
    print('Forma um triangulo3')
else:
    print('Não forma')'''

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo!')
else:
    print('Os segmentos acima nao formam um triangulo!')