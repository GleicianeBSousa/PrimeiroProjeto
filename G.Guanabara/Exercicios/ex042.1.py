#Alisson
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))
if r1 != r2 and r1 != r3 and r2 != r3:
    print('Escaleno')
elif r1 == r2 == r3:
    print('Equilatero')
elif r1 == r2 or r2 == r1 or r3 == r1 or r1 == r3 or r2 == r3 or r3 == r2:
    print('Isosceles')