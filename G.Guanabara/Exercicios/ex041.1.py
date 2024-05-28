#Alisson
import datetime
nascimento = int(input('\033[1;46mDigite a data de nascimento\033[m '))
ano_atual = datetime.date.today().year
categoria = ano_atual - nascimento
if categoria <= 9:
    print('\033[1;31mMirim\033[m')
elif categoria <= 14:
    print('\033[1;32mInfantil\033[m')
elif categoria <= 19:
    print('\033[1;33mJunior\033[m')
elif categoria <= 20:
    print('\033[1;34mSenior\033[m')
elif categoria > 20:
    print('\033[1;35mMaster\033[m')
else:
    print('\033[1;36mOpção invalida!\033[m')