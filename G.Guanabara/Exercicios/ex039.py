'''
    Faça um programa  que leia o ano de nascimento de um jovem e informe, de acordo com  a sua idade:

    se ele ainda vai se alistar ao serviço militar.
    se é a hora de se alistar
    se ja passou do tempo de alistamento

    seu programa tambem devera mostrar o tempo que faltou ou que passou do prazo
'''
# Rodrigo
from datetime import date

sexo = str(input("Digite [M] Se você é do sexo Masculino\nDigite [F] Se você for do sexo Feminio!").upper())

if sexo == "F":
    print("\033[1;4;45mVocê não precisa se Alistar!\033[m ")

elif sexo == "M":
    print("\033[1;4;42mPodemos seguir!\033[m")

    ano_nascimento = int(input("Digite a Data do Seu Nascimento! "))  
    ano_atual = date.today().year
    ano_alistamento = ano_atual - ano_nascimento

    if ano_alistamento < 18:
        print(f"\033[1;4;43mVocê têm {ano_alistamento} Anos, Ainda não tem Idade para o Alistamneto\033[m ")
        tempo_passado = 18 - ano_alistamento
        print(f"Ainda Falta \033[1;4;41m {tempo_passado} \033[mAnos Para o Alistamento ")

    elif ano_alistamento == 18:
        print(f" Você tem {ano_alistamento} Anos, Já está na Hora de Se Alistar. ")

    else:
        tempo_passado = ano_alistamento - 18
        print(f"\033[1;4;41mVocê Deveria Ter se Alistado há {tempo_passado} Anos Atrás, Procure um Posto de Alistamento Mais Próximo.\033[m ")    

else:
    print("Opção inválida, tente outra vez. ")    


#Alisson
ano_nasciment = input('Digite seu ano de nascimento até 4 digitos! ').strip()[:4]
num = int(ano_nasciment)
print(num)

if num >= 2007:
    print('\033[1;33mAinda vai se alistar!\033[m')
    print('\033[1;33mfalta \033[1;42m{}\033[m \033[1;33mde anos para se alistar\033[m'.format(num - 2007))
elif num == 2006:
    print('\033[1;32mÉ hora de se alistar!\033[m')
elif num < 2006:
    print('\033[1;31mJá passou da hora de se alistar!\033[m')
    print('\033[1;31mVoce deveria ter se alistado há\033[m \033[1;41m{}\033[m \033[1;31manos atras\033[m'.format(2006 - num))
else:
    print('\033[1;34mOpção invalida, tente novamente!\033[m')

