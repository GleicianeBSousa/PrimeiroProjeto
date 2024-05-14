'''
    Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

        A  Telefonou para a vítima?"
        B  Esteve no local do crime?"
        C  Mora perto da vítima?"
        D  Devia para a vítima?"
        E  Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
        
'''
#a receb sim ou nao
perg1 = str(input('Telefonou para a vítima? '))
perg2 = str(input('esteve no local do crime? '))
perg3 = str(input('Mora perto da vítima? '))
perg4 = str(input('Devia para vítima? '))
perg5 = str(input('Já trabalhou com a vítima? '))

if perg1 == 'Sim':
    if perg2 == 'Sim':
        if perg3 == 'Sim':
            if