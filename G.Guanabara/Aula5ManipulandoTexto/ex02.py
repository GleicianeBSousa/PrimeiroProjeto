frase = 'Curso em video python'
ab = '   Aprenda Python   '
#Analise
print(len(frase))
print(frase.count('e'+'o'))
print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))
print(frase.count('o', 0, 13))
print(frase.count('o', 0, 14))
print(frase.find('deo'))
print(frase.find('  '))
print(frase.find(' '))
print('curso' in frase)
print('Curso' in frase)
