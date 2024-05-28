#Alisson
peso = float(input('\033[1;44mPeso:\033[m '))
altura = float(input('\033[1;45mAltura:\033[m '))
imc = peso / altura **2
print('\033[1;46mO imc é:\033[m {:.2f}'.format(imc))
if imc < 18.5:
    print('\033[1;31mAbaixo do peso\033[m')
elif imc < 25:
    print('\033[1;32mPeso ideal\033[m')
elif imc < 30:
    print('\033[1;33mSobrepeso\033[m')
elif imc < 40:
    print('\033[1;34mObesidade\033[m')
elif imc > 40:
    print('\033[1;35mObesidade morbita\033[m')
else:
    print('\033[1;36mOpção invalida\033[m')