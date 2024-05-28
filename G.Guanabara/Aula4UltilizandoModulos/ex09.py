import math
oposto = float(input('Digite o cateto oposto: '))
adjacente = float(input('Digite o cateto adjacente: '))
soma = oposto**2 + adjacente**2
hipotenuza = math.sqrt(soma)
sen = oposto/hipotenuza
cos = adjacente/hipotenuza
tan = oposto/adjacente
print('')