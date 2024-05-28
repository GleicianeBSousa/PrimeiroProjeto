numeros = []
i = 1
while(i < 11):
    numero = int(input(f"Digite {i}° numero: "))
    numeros.append(numero)
    i += 1
   
maior = max(numeros)
menor = min(numeros)
media = sum(numeros) / len(numeros)

print(f"O maior número é o {maior}, o menor é o {menor} e a media é {media}")