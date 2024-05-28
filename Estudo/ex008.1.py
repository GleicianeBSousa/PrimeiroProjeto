a = int(input("digite um número "))
b = int(input("digite o segundo número "))
c = int(input("digite o terceiro número "))

maior = max(a, b, c)
menor = min(a, b, c)
meio = a + b + c - maior - menor 

print(f"maior numero:{maior}")  
print(f"menor numero: {menor}")
print(f"numero intermediário:{meio}")    

