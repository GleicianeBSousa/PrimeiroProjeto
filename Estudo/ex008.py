a = int(input("digite um número "))
b = int(input("digite o segundo número "))
c = int(input("digite o terceiro número "))

maior = max(a, b, c)
menor = min(a, b, c)

if a != maior and a != menor:
    intermediario = a
elif b != maior and b != menor:
    intermediario = b
else:
    intermediario = c

print('Maior numero: ', maior)
print('Menor numero: ', menor)
print('Numero intermediario: ', intermediario)