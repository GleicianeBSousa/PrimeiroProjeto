'''
    Escreva um programa que leia uma temperatura, pergunte a unidade dessa temperatura e converta o valor para as demais unidades (As unidades de temperatura são Celsius, Kelvin e Fahrenheit)
'''

temperatura = float(input('Digite o valor de uma temperatura: '))
celsius = temperatura
faren = temperatura * 1.8 + 32
kelvin = temperatura + 273.15
print("")
print("[ 1 ] para celsius\n[ 2 ] para farenhite\n[ 3 ] para kelvin")
print("")
escolha = int(input('Escolha uma opção de temperatura! '))
print("")
if escolha == 1:#Se escolhar for igual há 1 entao faça isso
    print('Você escolheu a temperatura de {}°C'.format(celsius))
elif escolha == 2:#Senão for verdade a opção acima entao faça isso
    print('Você escolheu a temperatura de {}°F'.format(faren))
elif escolha == 3:#Senão for verdade a opção acima entao faça isso
    print('Você escolheu a temperatura de {}°K'.format(kelvin))
else:#Se nenhuma opção for verdade entao faça isso
    print('Escolha invalida, digite uma das opções apresentadas')


